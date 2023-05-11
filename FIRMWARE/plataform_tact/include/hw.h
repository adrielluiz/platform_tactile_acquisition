#pragma once

// MPU
#define MPU_PIN_SCL PB6
#define MPU_PIN_SCA PB7

// Motor 1
#define MOTOR1_PIN1 PB15 //PB7
#define MOTOR1_PIN2 PB14 //PB2
#define MOTOR1_PIN3 PB13 //PB5
#define MOTOR1_PIN4 PB12 //PB4

// Motor 2
#define MOTOR2_PIN1 PB10 
#define MOTOR2_PIN2 PB2  
#define MOTOR2_PIN3 PB1  
#define MOTOR2_PIN4 PB0  

// Serial
#define SERIAL_PIN_TX PA2 //Branco
#define SERIAL_PIN_RX PA3 //Verde

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size);
void hw_timer_delay_ms(uint16_t delay_ms);
void hw_serial_init(uint32_t baud);
uint32_t hw_timer_get_tick_ms(void);
uint32_t hw_timer_elapsed_ms(uint32_t start);
