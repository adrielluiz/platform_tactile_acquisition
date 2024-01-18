#include <Arduino.h>
#include <BasicStepperDriver.h>
#include "motor.h"
#include "hw.h"

#define MOTOR_FULL_STEP 1
#define MAX_STEPS_RELEASE_END_STOP 10
#define MOTOR_HOME_SPEED 30
#define MOTOR_STEPS_REV 200
#define MOTOR_INITIAL_SPEED_RPM 300
#define MOTOR1_uM_REV 12000
#define MOTOR2_UM_REV 8000
#define MOTOR1_STEP_TO_uM 200.0 / 12000.0
#define MOTOR2_STEP_TO_uM 200.0 / 8000.0

BasicStepperDriver motor[2] = {BasicStepperDriver(MOTOR_STEPS_REV, MOTOR1_DIR_PIN, MOTOR1_STP_PIN), BasicStepperDriver(MOTOR_STEPS_REV,  MOTOR2_DIR_PIN, MOTOR2_STP_PIN)};

volatile int motor_pos_step[2] = {0,0};
volatile int motor_pos_um[2] = {0,0};
long int motor_max_dist_um[2] = {PLATAFORM_MAX_DIST_X_uM, PLATAFORM_MAX_DIST_Z_uM};
int motor_steps_realease_end_stop[2] = {-MAX_STEPS_RELEASE_END_STOP, MAX_STEPS_RELEASE_END_STOP};

void motor_init(void)
{ 
    motor[0].begin(MOTOR_INITIAL_SPEED_RPM, MOTOR_FULL_STEP);
    motor[1].begin(MOTOR_INITIAL_SPEED_RPM, MOTOR_FULL_STEP);
}

bool motor_move(int motor_id, int step)
{
    step = step * (-1);
    
    motor[motor_id-1].startMove(step);

    while (motor[motor_id-1].nextAction() != 0) 
    {
        if(hw_sw_is_on(motor_id-1))
        {
            motor[motor_id-1].stop();
            return false;
        }
    }

    return true;
}

void motor_set_speed(int motor_id, int speed_rpm)
{
    motor[motor_id].setRPM(speed_rpm);         
}

uint16_t motor_get_speed(int motor_id)
{
    return (uint16_t) motor[0].getRPM();    
}

int motor_convert_um_steps(int motor_id, int pos_um)
{
    double um_to_step;
    
    if(motor_id == 1)
        um_to_step = MOTOR1_STEP_TO_uM * pos_um;
    else if(motor_id == 2)
        um_to_step = MOTOR2_STEP_TO_uM * pos_um;  
    return (int) um_to_step;
}

void motor_set_pos(int motor_id, int pos_um)
{
    int new_pos_um = pos_um;
   
    if(new_pos_um > motor_max_dist_um[motor_id-1])
        new_pos_um = motor_max_dist_um[motor_id-1];

    new_pos_um = new_pos_um - motor_pos_um[motor_id -1];
        
    int pos_steps = motor_convert_um_steps(motor_id, new_pos_um);

    if(motor_move(motor_id, pos_steps))
        motor_pos_um[motor_id -1] = pos_um;
    else
        motor_pos_um[motor_id -1] = 0;
}

int motor_get_pos(int motor_id)
{
    return motor_pos_um[motor_id-1];    
}

void motor_set_pos_home(int motor_id)
{
    int pos_steps = motor_convert_um_steps(motor_id, motor_max_dist_um[motor_id-1]);

    // find end stop
  
    motor[motor_id-1].startMove(pos_steps);

    while (motor[motor_id-1].nextAction() != 0) 
    {
        if(hw_sw_is_on(motor_id-1))
        {
            motor[motor_id-1].stop();
            break;
        }
    }

    hw_timer_delay_ms(100);

    // release end stop

    motor[motor_id-1].startMove(-400);

    while (motor[motor_id-1].nextAction() != 0) 
    {
        if(!hw_sw_is_on(motor_id-1))
        {
            hw_timer_delay_ms(10);
            motor[motor_id-1].stop();
            break;
        }
    }
    
    motor_pos_um[motor_id -1] = 0;
}

void motor_test_loop(void)
{
    motor_move(1, 1000);
    motor_move(1, -1000);

    hw_timer_delay_ms(5000);
}