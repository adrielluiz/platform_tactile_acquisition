#include <Arduino.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdalign.h>
#include <stdlib.h>
#include "hw.h"

volatile bool end_stop_x = false; 
volatile bool end_stop_z = false; 
volatile bool flag_pos_home_x = false;
volatile bool flag_pos_home_z = false;

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
		if(digitalRead(SW1_PIN))
			end_stop_x = false;
		else
			end_stop_x = true;	

		deboucing_time_ms = millis();

		Serial.println("end_stop_x %d" + String(end_stop_x));

		flag_pos_home_x = false;
	}
}

void hw_sw2_isr()
{
	static uint32_t deboucing_time_ms = 0;

	if((millis() - deboucing_time_ms) >= HW_DEBOUCING_TIME_MS)
	{
		if(digitalRead(SW2_PIN))
			end_stop_z = false;
		else
			end_stop_z = true;	

		deboucing_time_ms = millis();

		Serial.println("end_stop_z %d" + String(end_stop_z));

		flag_pos_home_z = false;
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


uint32_t hw_fsr_read(void)
{
	return analogRead(FSR_PIN);
}

uint32_t hw_vs_read(void)
{
	return analogRead(VS_PIN);
}

void hw_init(void)
{
	pinMode(SW1_PIN, INPUT_PULLUP);
	pinMode(SW2_PIN, INPUT_PULLUP);

	pinMode(FSR_PIN, INPUT);

	attachInterrupt(digitalPinToInterrupt(SW1_PIN), hw_sw1_isr, RISING);
	attachInterrupt(digitalPinToInterrupt(SW2_PIN), hw_sw2_isr, RISING);

	hw_serial_init(SERIAL_BAUDRATE);

	flag_pos_home_x = digitalRead(SW1_PIN);
	flag_pos_home_z = digitalRead(SW2_PIN);	
}