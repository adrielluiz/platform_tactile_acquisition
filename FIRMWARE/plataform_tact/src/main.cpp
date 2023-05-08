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
  //Serial.println("Hello");
  //delay(1000);

  //mpu_read();

  app_loop();

}

