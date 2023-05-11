#pragma once

void motor_init(void);
void motor_set_speed(int motor, int speed_ms);
uint16_t motor_get_speed(int motor);
void motor_set_pos(int motor, int pos_mm);
uint16_t motor_get_pos(int motor);
