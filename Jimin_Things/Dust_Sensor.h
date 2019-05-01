#ifndef Dust_Sensor_h
#define Dust_Sensor_h


#include <Arduino.h>
#include <LiquidCrystal.h> 

// initialize the library with the numbers of the interface pins

class Dust_Sensor
{
public:
	//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
	//LiquidCrystal lcd;

	int error;
	int Meansuring_Times = 50;

	int Vo = A0;
	int V_LED = 8;

	float Vo_value = 0;
	float Voltage = 0;
	float dustDensity = 0;
	float dustCleanVoltage = 0.58; //초기값으로 보정요구 

	int samplingTime = 280;
	int deltaTime = 40;
	int sleepTime = 9680;

	void Init();

	void Computing_Mean();

	void Computing_dust();

	void PrintSerial();

	void PrintLCD();

	void Main_Logic();

};


#endif