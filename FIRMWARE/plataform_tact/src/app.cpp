#include <Arduino.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdalign.h>
#include <stdlib.h>
#include "app.h"
#include "cmd.h"
#include "cbuf.h"
#include "hw.h"
#include "mpu.h"
#include "motor.h"

volatile app_mode_t app_mode = APP_MODE_IDLE;
volatile bool app_started = false;
app_data_read_t data_read;

#define APP_ADD_MSG(m) app_uc2usb_rx_cbk((uint8_t *)(m), strlen((char *)(m)));

CBUF_DECLARE(app_uc2usb_cb,APP_MAX_BUFFER_SIZE);
CBUF_DECLARE(app_usb2uc_cb,APP_MAX_BUFFER_SIZE);

void app_usb2uc_rx_cbk() // interrupção serial rx
{
	uint8_t buffer[APP_MAX_CMDLINE_SIZE];
	uint32_t size;

	if(app_started)
	{
		if(Serial.available())
		{
			size = Serial.readBytes(buffer, APP_MAX_CMDLINE_SIZE);

			for(uint32_t n = 0 ; n < size ; n++)
			{
				while(cbuf_put(&app_usb2uc_cb,buffer[n]) != UTIL_CBUF_OK)
				{}
			}
		}


	}
}

void app_uc2usb_rx_cbk(uint8_t* buffer, uint32_t size)
{
	if(app_started)
	{
		for(uint32_t n = 0 ; n < size ; n++)
		{
			while(cbuf_put(&app_uc2usb_cb,buffer[n]) != UTIL_CBUF_OK)
			{}
		}
	}
}

void app_set_mode(app_mode_t mode)
{
	app_mode = mode;
}

app_mode_t app_get_mode(void)
{
	return app_mode;
}

void app_set_motor_speed(int motor, int speed_ms)
{
	motor_set_speed(motor,speed_ms);
}

uint16_t app_get_motor_speed(int motor)
{
	return motor_get_speed(motor);
}

void app_set_motor_pos(int motor, int pos_mm)
{
	motor_set_pos(motor,pos_mm);
}

uint16_t app_get_motor_pos(int motor)
{
	return motor_get_pos(motor);
}

mpu_data_t* app_get_mpu(void)
{
	return mpu_get();
}

void app_set_read(bool motors_flag, bool mpu_flag)
{
	data_read.motors = motors_flag;
	data_read.mpu = mpu_flag;
}

void app_set_read_delay_ms(uint32_t delay_ms)
{
	data_read.delay_ms = delay_ms;
}

uint32_t app_get_read_delay_ms(void)
{
	return data_read.delay_ms;
}

static void app_proc_idle(app_mode_state_t state)
{
	static uint32_t start_time_ms;
	static char buffer[32];

	switch(state)
	{
	case APP_MODE_STATE_INIT:
		snprintf(buffer,64,"mode idle\n");
		APP_ADD_MSG(buffer);
		break;
	case APP_MODE_STATE_RUN:
		break;
	case APP_MODE_STATE_STOP:
	default:
		break;
	}
}

static void app_proc_read(app_mode_state_t state)
{
	static uint32_t start_time_ms;
	static char buffer[64];
	mpu_data_t* mpu_data;
	int pos1 = 0;
	int pos2 = 0;

	switch(state)
	{
	case APP_MODE_STATE_INIT:
		start_time_ms = hw_timer_get_tick_ms();
		snprintf(buffer,64,"mode read\n");
		APP_ADD_MSG(buffer);
		break;
	case APP_MODE_STATE_RUN:
		if(hw_timer_elapsed_ms(start_time_ms) > data_read.delay_ms)
		{
			if(data_read.motors)
			{
				pos1 = app_get_motor_pos(1);
				pos2 = app_get_motor_pos(2);

				snprintf(buffer,64,"position %d %d\n", pos1, pos2);
				APP_ADD_MSG(buffer);
			}
			if(data_read.mpu)
			{
				mpu_data = app_get_mpu();

				snprintf(buffer,64,"mpu  %d %d %d %d %d %d %d\n",mpu_data->AcX, mpu_data->AcY, mpu_data->AcZ, mpu_data->Tmp,
																mpu_data->GyX, mpu_data->GyY, mpu_data->GyZ);
				APP_ADD_MSG(buffer);
			}

			start_time_ms = hw_timer_get_tick_ms();
		}
		break;
	case APP_MODE_STATE_STOP:
	default:
		break;
	}
}


static void app_proc(app_mode_t new_mode)
{
	void (*app_mode_funcs[])(app_mode_state_t state) = {app_proc_idle, app_proc_read};
	static app_mode_t last_mode = APP_MODE_IDLE;

	if(last_mode != new_mode)
	{
		app_mode_funcs[last_mode](APP_MODE_STATE_STOP);
		app_mode_funcs[new_mode](APP_MODE_STATE_INIT);
	}

	app_mode_funcs[new_mode](APP_MODE_STATE_RUN);

	last_mode = new_mode;
}

static void app_in(void)
{
	uint8_t c;
	static uint8_t cmdline[APP_MAX_CMDLINE_SIZE];
	static uint32_t pos = 0;

	while(cbuf_get(&app_usb2uc_cb,&c) == UTIL_CBUF_OK)
	{
		if(pos >= APP_MAX_CMDLINE_SIZE)
			pos = 0;

		cmdline[pos++] = c;

		if(c == '\n')
		{
			// process one command per run
			cmdline[pos-1] = '\0';
			cmd_proc(cmdline,pos);
			pos = 0;
			break;
		}
	}
}

void app_out(void)
{
	uint8_t c;
	static uint8_t cmdline[APP_MAX_CMDLINE_SIZE];
	static uint32_t pos = 0;
	static uint8_t n_retries = 0;
	static bool in_retransmission = false;

	if(!in_retransmission)
	{
		while(cbuf_get(&app_uc2usb_cb,&c) == UTIL_CBUF_OK)
		{
			cmdline[pos++] = c;

			if((c == '\n') || (pos >= APP_MAX_CMDLINE_SIZE))
			{
				// process one line per run
				cmdline[pos++] = '\0';
				if(hw_usb_tx_data(cmdline,pos))
				{
					//hw_timer_delay_ms(15);
					memset(cmdline, 0, pos);
					pos = 0;
				}
				else
					in_retransmission = true;

				n_retries = 0;

				break;
			}
		}
	}
	else
	{
		// short circuit evaluation
		if(++n_retries >= 3 || hw_usb_tx_data(cmdline,pos))
		{
			in_retransmission = false;
			n_retries = 0;
			pos = 0;
			hw_timer_delay_ms(15);
		}
	}

}



void app_init(void)
{
	cbuf_init(&app_uc2usb_cb);
    cbuf_init(&app_usb2uc_cb);

	hw_serial_init(115200);
	mpu_init();
	motor_init();

	data_read.motors = false;
	data_read.mpu = false;
	data_read.delay_ms = 100;

	app_started = true;
}

void app_loop(void)
{
	app_usb2uc_rx_cbk();

	app_in();
	app_proc(app_mode);
	app_out();
}
