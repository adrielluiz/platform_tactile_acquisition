#include <Arduino.h>
#include <Stepper.h>
#include "motor.h"
#include "hw.h"


const int stepsPerRevolution = 25600;  // change this to fit the number of steps per revolution

Stepper motor1(stepsPerRevolution, MOTOR1_PIN1, MOTOR1_PIN2, MOTOR1_PIN3, MOTOR1_PIN4);
Stepper motor2(stepsPerRevolution, MOTOR2_PIN1, MOTOR2_PIN2, MOTOR2_PIN3, MOTOR2_PIN4);

volatile uint16_t motor1_speed = 60;
volatile uint16_t motor2_speed = 60;
volatile uint16_t motor1_pos_step = 0;
volatile uint16_t motor2_pos_step = 0;

void motor_init(void)
{ 
    motor1.setSpeed(60);
    motor2.setSpeed(60);
}

void motor_move(int motor, int step)
{
    if(motor == 1)
        motor1.step(step);
    else if(motor == 2)
        motor2.step(step);
}

void motor_set_speed(int motor, int speed_ms)
{
    if(motor == 1)
    {
        motor1_speed = speed_ms;
        motor1.setSpeed(speed_ms);
    }
        
    else if(motor == 2)
    {
        motor2_speed = speed_ms;
        motor2.setSpeed(speed_ms);
    }
        
}

uint16_t motor_get_speed(int motor)
{
    if(motor == 1)
        return motor1_speed;
    else if(motor == 2)
        return motor2_speed;

    return 0;    
}

int motor_convert_mm_steps(int mm)
{
    return mm+1;
}

void motor_set_pos(int motor, int pos_mm)
{
    int pos_steps = motor_convert_mm_steps(pos_mm);

    if(motor == 1)
    {
        motor_move(1, pos_steps - motor1_pos_step);
        //motor1.step(pos_mm);
        motor1_pos_step = pos_steps;
    }
    else if(motor == 2)
    {
        motor_move(2, pos_steps - motor2_pos_step);
       // motor2.step(pos_mm);
        motor2_pos_step = pos_steps;
    }        
}

uint16_t motor_get_pos(int motor)
{
    if(motor == 1)
        return motor1_pos_step;
    else if(motor == 2)
        return motor2_pos_step;

    return 0;    
}

