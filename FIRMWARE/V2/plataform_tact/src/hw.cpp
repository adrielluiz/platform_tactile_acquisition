#include <Arduino.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdalign.h>
#include <stdlib.h>
#include "hw.h"
#include "app.h"

HardwareTimer timer_app(TIM1);
HardwareTimer timer_usb_tx(TIM2);

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

bool hw_sw_is_on(int axis)
{
	if(axis == AXIS_X )
		return digitalRead(SW1_PIN);
	else if(axis == AXIS_Z)	
		return digitalRead(SW2_PIN);
		
	return false;	
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

void hw_timer_app_cbk(void)
{
	app_timer_cbk();
}

void hw_timer_app_config(uint16_t freq)
{
	timer_app.setPrescaleFactor(1000); // Set prescaler to 10000 => timer frequency = 84MHz/10K = 84.000 Hz 
    timer_app.setOverflow(8400/freq); // Set overflow
    timer_app.attachInterrupt(hw_timer_app_cbk);
    timer_app.refresh(); // Make register changes take effect
    timer_app.resume(); // Start
}

void hw_timer_app_init(void)
{
	hw_timer_app_config(INIT_READ_FREQ);
}

void hw_restart(void)
{
	HAL_NVIC_SystemReset();
}

void hw_init(void)
{
	pinMode(SW1_PIN, INPUT_PULLDOWN);
	pinMode(SW2_PIN, INPUT_PULLDOWN);

	pinMode(FSR_PIN, INPUT);

	hw_serial_init(SERIAL_BAUDRATE);

	hw_timer_app_init();
	hw_timer_usb_tx_init();
}