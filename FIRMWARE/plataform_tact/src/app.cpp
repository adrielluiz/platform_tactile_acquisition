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

static void app_proc_idle(app_mode_state_t state)
{
	static uint32_t start_time_ms;
	static char buffer[32];

	switch(state)
	{
	case APP_MODE_STATE_INIT:

		break;
	case APP_MODE_STATE_RUN:

		break;
	case APP_MODE_STATE_STOP:

	default:
		break;
	}
}


static void app_proc(app_mode_t new_mode)
{
	void (*app_mode_funcs[])(app_mode_state_t state) = {app_proc_idle};
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
				if(hw_usb_tx_data(cmdline,pos))
				{
					hw_timer_delay_ms(15);
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
	hw_serial_init(115200);
	mpu_init();
	motor_init();

	app_started = true;
}

void app_loop(void)
{
	app_usb2uc_rx_cbk();

	app_in();
	app_proc(app_mode);
	app_out();
}
