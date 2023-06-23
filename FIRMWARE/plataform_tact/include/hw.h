#pragma once

#define SERIAL_BAUDRATE 230400 //921600 //115200 
#define HW_DEBOUCING_TIME_MS 50
#define AXIS_X 0
#define AXIS_Z 1
#define PLATAFORM_MAX_DIST_X_MM 100
#define PLATAFORM_MAX_DIST_Z_MM 50
#define PLATAFORM_MAX_DIST_X_uM 1700000
#define PLATAFORM_MAX_DIST_Z_uM 40000


// MPU
#define MPU_ADDR 0x68
#define MPU_PIN_SCL PB6
#define MPU_PIN_SCA PB7

// Motor 1
#define MOTOR1_PIN1 PB15 //PB7
#define MOTOR1_PIN2 PB14 //PB2
#define MOTOR1_PIN3 PB13 //PB5
#define MOTOR1_PIN4 PB12 //PB4

// Motor 2 (1.2 A)
#define MOTOR2_PIN1 PB10 
#define MOTOR2_PIN2 PB2  
#define MOTOR2_PIN3 PB1  
#define MOTOR2_PIN4 PB0  

// Serial
#define SERIAL_PIN_TX PA2 //Branco
#define SERIAL_PIN_RX PA3 //Verde

// Limit Switch
#define SW1_PIN PB8
#define SW2_PIN PB9

// FSR
#define FSR_PIN PA0 //PA6

// Voltage Sensor
#define VS_PIN PA6

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size);
void hw_timer_delay_ms(uint16_t delay_ms);
void hw_serial_init(uint32_t baud);
uint32_t hw_timer_get_tick_ms(void);
uint32_t hw_timer_elapsed_ms(uint32_t start);
void hw_set_flag_pos_home(bool state);
void hw_set_flag_pos_home_x(void);
void hw_set_flag_pos_home_z(void);
bool hw_get_flag_pos_home_x_start(void);
bool hw_get_flag_pos_home_z_start(void);
uint32_t hw_fsr_read(void);
uint32_t hw_vs_read(void);
bool hw_sw_is_on(int axis, int dir);
void hw_init(void);