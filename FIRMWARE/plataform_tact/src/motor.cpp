#include <Arduino.h>
#include <Stepper.h>
#include "motor.h"
#include "hw.h"

#define MOTOR_HOME_SPEED 30
const int stepsPerRevolution = 25600;  // change this to fit the number of steps per revolution

Stepper motor[2] = {Stepper(stepsPerRevolution, MOTOR1_PIN1, MOTOR1_PIN2, MOTOR1_PIN3, MOTOR1_PIN4), Stepper(stepsPerRevolution, MOTOR2_PIN1, MOTOR2_PIN2, MOTOR2_PIN3, MOTOR2_PIN4)};

volatile uint16_t motor_speed[2] = {60,60};
volatile uint16_t motor_pos_step[2] = {0,0};

void motor_init(void)
{ 
    motor[0].setSpeed(motor_speed[0]);
    motor[0].setAxis(AXIS_X);
    motor[1].setSpeed(motor_speed[1]);
    motor[1].setAxis(AXIS_Z);
}

void motor_move(int motor_id, int step)
{
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

int motor_convert_mm_steps(int mm)
{
    return mm+1;
}

void motor_set_pos(int motor_id, int pos_mm)
{
    //int pos_steps = motor_convert_mm_steps(pos_mm);

    motor[motor_id-1].step(pos_mm);

/*    if(motor == 1)
    {
        //motor_move(1, pos_steps - motor1_pos_step);
        motor1.step(pos_mm);
        //motor1_pos_step = pos_steps;
    }
    else if(motor == 2)
    {
        //motor_move(2, pos_steps - motor2_pos_step);
        motor2.step(pos_mm);
        //motor2_pos_step = pos_steps;
    }       */ 
}

uint16_t motor_get_pos(int motor_id)
{
    return motor_pos_step[motor_id-1];    
}

void motor_set_pos_home(int motor_id)
{
    motor[motor_id-1].setSpeed(MOTOR_HOME_SPEED);

    if(motor_id == 1)
    {
        motor[0].step(PLATAFORM_MAX_DIST_X_MM);
        hw_set_flag_pos_home_x();
    }
    else if(motor_id == 2)
    {
        motor[0].step(-PLATAFORM_MAX_DIST_Z_MM);
        hw_set_flag_pos_home_z();
    }

     motor[motor_id-1].setSpeed(motor_speed[motor_id]);
}
