#pragma once

#define SERIAL_BAUDRATE 230400 //921600 //115200 
#define HW_DEBOUCING_TIME_MS 50
#define AXIS_X 0
#define AXIS_Z 1
#define PLATAFORM_MAX_DIST_X_MM 100
#define PLATAFORM_MAX_DIST_Z_MM 50
#define PLATAFORM_MAX_DIST_X_uM 1700000
#define PLATAFORM_MAX_DIST_Z_uM 40000
#define INIT_READ_FREQ 10

// MPU
#define MPU_ADDR 0x68
#define MPU_PIN_SCL PB6
#define MPU_PIN_SCA PB7

//motor x
#define MOTOR1_DIR_PIN PB14
#define MOTOR1_STP_PIN PB15

//motor z
#define MOTOR2_DIR_PIN PB12
#define MOTOR2_STP_PIN PB13

// Serial
#define SERIAL_PIN_TX PA2 //Branco
#define SERIAL_PIN_RX PA3 //Verde

// Limit Switch
#define SW1_PIN PA6
#define SW2_PIN PA5

// FSR
#define FSR_PIN PA0 //PA6

// Voltage Sensor
#define VS_PIN PA6

// Driver Stepper: drv8825 
// https://github.com/RobTillaart/DRV8825

bool hw_usb_tx_data(uint8_t *buffer, uint8_t size);
void hw_timer_delay_ms(uint16_t delay_ms);
void hw_serial_init(uint32_t baud);
uint32_t hw_timer_get_tick_ms(void);
uint32_t hw_timer_elapsed_ms(uint32_t start);
uint32_t hw_fsr_read(void);
uint32_t hw_vs_read(void);
bool hw_sw_is_on(int axis);
void hw_restart(void);
void hw_timer_app_config(uint16_t freq);
void hw_init(void);