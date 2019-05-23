#ifndef Dust_Sensor_h
#define Dust_Sensor_h

#include <stdio.h>
#include <time.h>


#include <Arduino.h>
#include <LiquidCrystal.h> 

using namespace std;
// initialize the library with the numbers of the interface pins

class Dust_Sensor
{
public:
	//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
	//LiquidCrystal lcd;
	bool ACK = false;
	int error;
	int Meansuring_Times = 10;

	int Vo = A0;
	int V_LED = 8;

	float Vo_value = 0;
	float Voltage = 0;
	float dustDensity = 0;
	float dustCleanVoltage = 0.63; //초기값으로 보정요구 

	const int samplingTime = 280;
	const int deltaTime = 40;
	const int sleepTime = 9680;

	void Init();

	void Computing_Mean();

	void Computing_dust();

	void PrintSerial();

	void PrintLCD();

	void Main_Logic();

private:
	tm currentDateTime();

};


#endif