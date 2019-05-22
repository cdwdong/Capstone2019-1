#include <Jimin_Things.h>

Dust_Sensor dust;
Fan_Things fan;

void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  fan.Init();
  dust.Init();
}

void loop() 
{
  // put your main code here, to run repeatedly:
  fan.Main_Logic();
  dust.Main_Logic();
}
