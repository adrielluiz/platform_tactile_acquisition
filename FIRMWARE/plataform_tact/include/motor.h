#pragma once

void motor_init(void);
void motor_set_speed(int motor_id, int speed_ms);
uint16_t motor_get_speed(int motor_id);
void motor_set_pos(int motor_id, int pos_mm);
uint16_t motor_get_pos(int motor_id);
void motor_set_pos_home(int motor_id);
