#include <Arduino.h>
#include "app.h"

void setup() 
{
  app_init();
  //app_set_motor_pos_home(1);
  //app_set_motor_pos_home(2);
}

void loop() 
{
  app_loop();
}
