#include <Arduino.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdalign.h>
#include <stdlib.h>
#include "hw.h"
#include "app.h"

HardwareTimer timer(TIM1);
HardwareTimer timer_usb_tx(TIM2);
volatile bool flag_pos_home_x = false;
volatile bool flag_pos_home_z = false;
volatile bool flag_pos_home_x_start = false;
volatile bool flag_pos_home_z_start = false;

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size)
{
	char buf_tx[100];
    memcpy(buf_tx,buffer,size);

    return Serial.print(buf_tx);
}

void hw_timer_delay_ms(uint16_t delay_ms)
{
    delay(delay_ms);
}

void hw_serial_init(uint32_t baud)
{
    Serial.begin(baud);
}

uint32_t hw_timer_get_tick_ms(void)
{
	return millis();
}

uint32_t hw_timer_elapsed_ms(uint32_t start)
{
	uint32_t elapsed;
	uint32_t now = hw_timer_get_tick_ms();

	if(now < start)
		elapsed = (HAL_MAX_DELAY - start) + now + 1;
	else
		elapsed = now - start;

	return elapsed;
}

void hw_sw1_isr()
{
	static uint32_t deboucing_time_ms = 0;

	if((millis() - deboucing_time_ms) >= HW_DEBOUCING_TIME_MS)
	{
		deboucing_time_ms = millis();
		flag_pos_home_x = false;

		Serial.println("end_x 0");
	}
}

void hw_sw2_isr()
{
	static uint32_t deboucing_time_ms = 0;

	if((millis() - deboucing_time_ms) >= HW_DEBOUCING_TIME_MS)
	{
		deboucing_time_ms = millis();
		flag_pos_home_z = false;

		Serial.println("end_z 0");
	}
}

bool hw_sw_is_on(int axis, int dir)
{
	if(axis == AXIS_X && ((flag_pos_home_x == false) ^ (dir < 0)))
		return !digitalRead(SW1_PIN);
	else if(axis == AXIS_Z  && ((flag_pos_home_z == false) ^ (dir > 0)))	
		return !digitalRead(SW2_PIN);
		
	return false;	
}

void hw_set_flag_pos_home(bool state)
{
	flag_pos_home_x = state;
	flag_pos_home_z = state;
}

void hw_set_flag_pos_home_x(void)
{
	flag_pos_home_x = true;
}

void hw_set_flag_pos_home_z(void)
{
	flag_pos_home_z = true;
}

bool hw_get_flag_pos_home_x_start(void)
{
	return flag_pos_home_x_start;
}

bool hw_get_flag_pos_home_z_start(void)
{
	return flag_pos_home_z_start;
}

uint32_t hw_fsr_read(void)
{
	return analogRead(FSR_PIN);
}

uint32_t hw_vs_read(void)
{
	return analogRead(VS_PIN);
}

void hw_timer_usb_tx_init(void)
{	
	timer_usb_tx.setPrescaleFactor(10000); // Set prescaler to 10000 => timer frequency = 84MHz/1000 = 8400 Hz 
    timer_usb_tx.setOverflow(8400/1000); // Set overflow
    timer_usb_tx.attachInterrupt(app_timer_usb_tx_cbk);
    timer_usb_tx.refresh(); // Make register changes take effect
    timer_usb_tx.resume(); // Start
}

void hw_timer_cbk(void)
{
    //Serial.println(millis());
	app_timer_cbk();
}

void hw_timer_config(uint16_t freq)
{
    //volatile uint32_t SysClockFreq = HAL_RCC_GetSysClockFreq(); 84 MHz

	timer.setPrescaleFactor(10000); // Set prescaler to 10000 => timer frequency = 84MHz/1000 = 8400 Hz 
    timer.setOverflow(8400/freq); // Set overflow
    timer.attachInterrupt(hw_timer_cbk);
    timer.refresh(); // Make register changes take effect
    timer.resume(); // Start
}

void hw_timer_init(void)
{
	hw_timer_config(INIT_READ_FREQ);
}

void hw_restart(void)
{
	HAL_NVIC_SystemReset();
}

void hw_init(void)
{
	pinMode(SW1_PIN, INPUT_PULLUP);
	pinMode(SW2_PIN, INPUT_PULLUP);

	pinMode(FSR_PIN, INPUT);

	attachInterrupt(digitalPinToInterrupt(SW1_PIN), hw_sw1_isr, RISING);
	attachInterrupt(digitalPinToInterrupt(SW2_PIN), hw_sw2_isr, RISING);

	hw_serial_init(SERIAL_BAUDRATE);

	flag_pos_home_x_start = !digitalRead(SW1_PIN);	
	flag_pos_home_z_start = !digitalRead(SW2_PIN);	

	hw_timer_init();
	hw_timer_usb_tx_init();

}