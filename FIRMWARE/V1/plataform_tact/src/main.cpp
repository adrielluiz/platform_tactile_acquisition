#include <Arduino.h>
//#include <Stepper.h>
#include <Wire.h>
#include "app.h"
#include "mpu.h"

void setup() 
{
  app_init();  
}

void loop() 
{
  app_loop();
}

