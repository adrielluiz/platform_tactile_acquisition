#pragma once
#include "mpu.h"

#define APP_MAX_CMDLINE_SIZE 128
#define APP_MAX_BUFFER_SIZE  (APP_MAX_CMDLINE_SIZE*47)

typedef enum app_mode_e
{
	APP_MODE_IDLE = 0,
	APP_MODE_READ,
} app_mode_t;

typedef enum app_mode_state_e
{
	APP_MODE_STATE_INIT = 0,
	APP_MODE_STATE_RUN,
	APP_MODE_STATE_STOP
} app_mode_state_t;

typedef struct app_data_read_e
{
    volatile bool motors; 
	volatile bool mpu;
	uint32_t delay_ms;
}app_data_read_t;


void app_init(void);
void app_loop(void);
void app_uc2usb_rx_cbk(uint8_t* buffer, uint32_t size);
void app_set_mode(app_mode_t mode);
app_mode_t app_get_mode(void);
void app_set_motor_speed(int motor, int speed_ms);
uint16_t app_get_motor_speed(int motor);
void app_set_motor_pos(int motor, int pos_mm);
void app_set_motor_pos_home(int motor);
uint16_t app_get_motor_pos(int motor);
mpu_data_t* app_get_mpu(void);
void app_set_read(bool motors_flag, bool mpu_flag);
void app_set_read_delay_ms(uint32_t delay_ms);
uint32_t app_get_read_delay_ms(void);
uint32_t app_get_fsr(void);
