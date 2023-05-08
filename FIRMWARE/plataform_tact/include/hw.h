#pragma once

// MPU
#define MPU_PIN_SCL PB6
#define MPU_PIN_SCA PB7

// Motor 1
#define MOTOR1_PIN1 PA7 //PB15
#define MOTOR1_PIN2 PA6 //PB14
#define MOTOR1_PIN3 PA5 //PB13
#define MOTOR1_PIN4 PA4 //PB12

// Motor 2
#define MOTOR2_PIN1 PB10 
#define MOTOR2_PIN2 PB2  
#define MOTOR2_PIN3 PB1  
#define MOTOR2_PIN4 PB0  

// Serial
#define SERIAL_PIN_TX PA2
#define SERIAL_PIN_RX PA3

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size);
void hw_timer_delay_ms(uint16_t delay_ms);
void hw_serial_init(uint32_t baud);
