#pragma once

#define MOTOR1_STEP_MM 12
#define MOTOR2_STEP_MM 8
#define MOTOR1_STEP_uM 12000
#define MOTOR2_STEP_uM 8000

void motor_init(void);
void motor_set_speed(int motor_id, int speed_ms);
uint16_t motor_get_speed(int motor_id);
void motor_set_pos(int motor_id, int pos_um);
uint16_t motor_get_pos(int motor_id);
void motor_set_pos_home(int motor_id);
