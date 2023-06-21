#include <Arduino.h>
#include <Stepper.h>
#include "motor.h"
#include "hw.h"

#define MOTOR_HOME_SPEED 20
const int stepsPerRevolution = 40000;  

Stepper motor[2] = {Stepper(stepsPerRevolution, MOTOR1_PIN1, MOTOR1_PIN2, MOTOR1_PIN3, MOTOR1_PIN4), Stepper(stepsPerRevolution, MOTOR2_PIN1, MOTOR2_PIN2, MOTOR2_PIN3, MOTOR2_PIN4)};

volatile uint16_t motor_speed[2] = {60,60};
volatile int motor_pos_step[2] = {0,0};
volatile int motor_pos_um[2] = {0,0};
int motor_max_dist_um[2] ={PLATAFORM_MAX_DIST_X_uM, PLATAFORM_MAX_DIST_Z_uM};

void motor_init(void)
{ 
    motor[0].setSpeed(motor_speed[0]);
    motor[0].setAxis(AXIS_X);
    motor[1].setSpeed(motor_speed[1]);
    motor[1].setAxis(AXIS_Z);
}

void motor_move(int motor_id, int step)
{
    if(motor_id == 1)
        step = step * (-1);
    
    motor[motor_id-1].step(step);
}

void motor_set_speed(int motor_id, int speed_ms)
{
    motor_speed[motor_id-1] = speed_ms;
    motor[motor_id-1].setSpeed(speed_ms);        
}

uint16_t motor_get_speed(int motor_id)
{
    return motor_speed[motor_id-1];    
}

int motor_convert_mm_steps(int motor_id, int pos_mm)
{
    double mm_to_step;
    
    if(motor_id == 1)
        mm_to_step = stepsPerRevolution/MOTOR1_STEP_MM * pos_mm;
    else if(motor_id == 2)
        mm_to_step = stepsPerRevolution/MOTOR2_STEP_MM * pos_mm;  
    return (int) mm_to_step;
}

int motor_convert_um_steps(int motor_id, int pos_um)
{
    double um_to_step;
    
    if(motor_id == 1)
        um_to_step = (stepsPerRevolution/MOTOR1_STEP_uM) * pos_um;
    else if(motor_id == 2)
        um_to_step = (stepsPerRevolution/MOTOR2_STEP_uM) * pos_um;  
    return (int) um_to_step;
}

void motor_set_pos(int motor_id, int pos_um)
{
    int new_pos_um = pos_um - motor_pos_um[motor_id -1];

    if(new_pos_um > motor_max_dist_um[motor_id-1])
        new_pos_um = motor_max_dist_um[motor_id-1];

    int pos_steps = motor_convert_um_steps(motor_id, new_pos_um);

    motor_move(motor_id, pos_steps);
    motor_pos_um[motor_id -1] = new_pos_um;
}

uint16_t motor_get_pos(int motor_id)
{
    return motor_pos_um[motor_id-1];    
}

void motor_set_pos_home(int motor_id)
{
    motor[motor_id-1].setSpeed(MOTOR_HOME_SPEED);

    if(motor_id == 1)
    {
        if(hw_get_flag_pos_home_x_start() == false)
        {
            motor_set_pos(1,-PLATAFORM_MAX_DIST_X_uM);
            hw_set_flag_pos_home_x();
        }

    }
    else if(motor_id == 2)
    {
        if(hw_get_flag_pos_home_z_start() == false)
        {
            motor_set_pos(2, -PLATAFORM_MAX_DIST_Z_uM);
            hw_set_flag_pos_home_z();
        }
    }

    motor[motor_id-1].setSpeed(motor_speed[motor_id]);
    motor_pos_um[motor_id -1] = 0;
}
