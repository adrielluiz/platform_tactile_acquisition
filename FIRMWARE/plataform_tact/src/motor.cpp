#include <Arduino.h>
#include <Stepper.h>
#include "motor.h"

const int stepsPerRevolution = 25600;  // change this to fit the number of steps per revolution

Stepper motor1(stepsPerRevolution, PA7, PA6, PA5, PA4);
Stepper motor2(stepsPerRevolution, PB10, PB2, PB1, PB0);

volatile uint16_t motor1_speed = 60;
volatile uint16_t motor2_speed = 60;

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
        motor1.step(step);
}

void motor_set_speed(int motor, int speed_ms)
{
    if(motor == 1)
        motor1_speed = speed_ms;
    else if(motor == 2)
        motor2_speed = speed_ms;
}

uint16_t motor_get_speed(int motor)
{
    if(motor == 1)
        return motor1_speed;
    else if(motor == 2)
        return motor2_speed;
}