#include <Arduino.h>
#include <AccelStepper.h>
#include <Wire.h>
#include "app.h"
#include "mpu.h"
#include "hw.h"
#include "motor.h"
#include "BasicStepperDriver.h"

#if 1
void setup() 
{
  app_init();
  //motor_init();
}

void loop() 
{
  app_loop();
  //motor_test_loop();
}
#endif

#if 0
#define MOTOR_STEPS 200
#define RPM 300

// Since microstepping is set externally, make sure this matches the selected mode
// If it doesn't, the motor will move at a different RPM than chosen
// 1=full step, 2=half step etc.
#define MICROSTEPS 1

//Uncomment line to use enable/disable functionality
//#define SLEEP 13

// 2-wire basic config, microstepping is hardwired on the driver
BasicStepperDriver stepper(MOTOR_STEPS, MOTOR2_DIR_PIN, MOTOR2_STP_PIN);

//Uncomment line to use enable/disable functionality
//BasicStepperDriver stepper(MOTOR_STEPS, DIR, STEP, SLEEP);

void setup() {
    stepper.begin(RPM, MICROSTEPS);
    // if using enable/disable on ENABLE pin (active LOW) instead of SLEEP uncomment next line
    // stepper.setEnableActiveState(LOW);
}

void loop() {
  
    // energize coils - the motor will hold position
    // stepper.enable();
  
    /*
     * Moving motor one full revolution using the degree notation
     */
    stepper.rotate(180);

    delay(5000);
    /*
     * Moving motor to original position using steps
     */
    stepper.rotate(-180);

    // pause and allow the motor to be moved by hand
    // stepper.disable();

    delay(5000);
}
#endif