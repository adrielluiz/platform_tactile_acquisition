#include <Arduino.h>
#include <AccelStepper.h>
#include "motor.h"
#include "hw.h"

#define MAX_STEPS_RELEASE_END_STOP 10
#define MOTOR_HOME_SPEED 30
const int stepsPerRevolution = 40000;  

AccelStepper motor[2] = {AccelStepper(AccelStepper::DRIVER, MOTOR1_PIN1, MOTOR1_PIN1), AccelStepper(AccelStepper::DRIVER, MOTOR1_PIN1, MOTOR1_PIN1)};

volatile uint16_t motor_speed[2] = {60,60};
volatile int motor_pos_step[2] = {0,0};
volatile int motor_pos_um[2] = {0,0};
long int motor_max_dist_um[2] = {PLATAFORM_MAX_DIST_X_uM, -PLATAFORM_MAX_DIST_Z_uM};
int motor_steps_realease_end_stop[2] = {-MAX_STEPS_RELEASE_END_STOP, MAX_STEPS_RELEASE_END_STOP};

void motor_init(void)
{ 
    motor[0].setMaxSpeed(100.0);
    motor[0].setAcceleration(100.0);
    motor[0].setSpeed(motor_speed[0]);

    motor[1].setMaxSpeed(100.0);
    motor[1].setAcceleration(100.0);
    motor[1].setSpeed(motor_speed[0]);
}

void motor_move(int motor_id, int step)
{
    if(motor_id == 1)
        step = step * (-1);
    
    motor[motor_id-1].move(step);
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
    int new_pos_um = pos_um;
    bool pos_reached = false;

    if(new_pos_um > motor_max_dist_um[motor_id-1])
        new_pos_um = motor_max_dist_um[motor_id-1];

    int pos_steps = motor_convert_um_steps(motor_id, new_pos_um);

    motor[motor_id-1].moveTo(pos_steps);

    while(!pos_reached)
    {
        pos_reached = motor[motor_id-1].run();
    }

    motor_move(motor_id, pos_steps);
    motor_pos_um[motor_id -1] = pos_um;
}

int motor_get_pos(int motor_id)
{
    return motor_pos_um[motor_id-1];    
}

void motor_set_pos_home(int motor_id)
{
    int pos_steps = motor_convert_um_steps(motor_id, motor_max_dist_um[motor_id - 1]);
    bool pos_reached = false;

    motor[motor_id-1].moveTo(pos_steps);
    motor[motor_id-1].setSpeed(MOTOR_HOME_SPEED);

    while(!hw_sw_is_on(motor_id - 1) && !pos_reached)
    {
        pos_reached = motor[motor_id-1].run();
    }

    // After reaching the limit switch, move in the opposite direction to release it.

    motor[motor_id-1].move(motor_steps_realease_end_stop[motor_id - 1]);

    while(hw_sw_is_on(motor_id - 1) && !pos_reached)
    {
        pos_reached = motor[motor_id-1].run();
    }

    motor[motor_id-1].setCurrentPosition(0);
    motor[motor_id-1].setSpeed(motor_speed[motor_id]);
}
