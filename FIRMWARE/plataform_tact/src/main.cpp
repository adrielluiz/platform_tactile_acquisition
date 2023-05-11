#include <Arduino.h>
#include <Stepper.h>
#include <Wire.h>
//#include "motor.h"
#include "app.h"
#include "mpu.h"
//#include "cbuf.h"
//#include "cmd.h"


void setup() 
{
  app_init();  
}

void loop() 
{
  app_loop();
}

