#pragma once

#define APP_MAX_CMDLINE_SIZE 128
#define APP_MAX_BUFFER_SIZE  (APP_MAX_CMDLINE_SIZE*47)

typedef enum app_mode_e
{
	APP_MODE_IDLE = 0,
	APP_MODE_RUN1,
} app_mode_t;


typedef enum app_mode_state_e
{
	APP_MODE_STATE_INIT = 0,
	APP_MODE_STATE_RUN,
	APP_MODE_STATE_STOP
} app_mode_state_t;

void app_init(void);
void app_loop(void);
void app_uc2usb_rx_cbk(uint8_t* buffer, uint32_t size);
void app_set_mode(app_mode_t mode);
app_mode_t app_get_mode(void);
