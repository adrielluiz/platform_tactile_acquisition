#include <Arduino.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdalign.h>
#include <stdlib.h>
#include "hw.h"

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size)
{
	static char buf_tx[100];
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