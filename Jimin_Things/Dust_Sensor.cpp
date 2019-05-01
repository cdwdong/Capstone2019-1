//﻿#pragma once

#include "Dust_Sensor.h"

void Dust_Sensor::Init()
{
	LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
	lcd.begin(16, 2);

	Serial.begin(9600);

	/*digital output:*/
	pinMode(V_LED, OUTPUT);

	/*analog input:*/
	pinMode(Vo, INPUT);

	lcd.clear();
	lcd.print("Booting......");
}

void Dust_Sensor::Computing_Mean()
{
	float mean = 0;
	float meanV = 0;

	Voltage = 0;
	dustDensity = 0;

	for (int i = 0; i < Meansuring_Times; i++)
	{
		Voltage = 0;
		dustDensity = 0;
		Computing_dust();
		mean = mean + dustDensity;
		meanV = meanV + Voltage;

		delay(100);
	}

	mean = mean / Meansuring_Times;
	meanV = meanV / Meansuring_Times;

	dustDensity = mean;
	Voltage = meanV;
}
void Dust_Sensor::Computing_dust()
{
	Vo_value = 0;
	Voltage = 0;

	digitalWrite(V_LED, LOW);  //ired 'on'
	delayMicroseconds(samplingTime);
	Vo_value = analogRead(Vo); //read the dust value
	delayMicroseconds(deltaTime);// pulse width 0.32 - 0.28 = 0.04 msec
								 //0.32 msec의 펄스폭을 유지하기 위해 필요한 코드입니다

	digitalWrite(V_LED, HIGH); //ired 'off'
	delayMicroseconds(sleepTime);


	/*
	이 센서의 출력전압(Vo)는 먼지가 없을 때의 출력전압(Voc)과 먼지 농도(ΔV)에 비례하여 출력됩니다.
	다시 표현하면 ΔV = Vo – Voc
	미세먼지 농도[µg/m³] = (Vo – Voc) / 0.005
	*/
	Voltage = Vo_value * (5.0 / 1024.0);

	dustDensity = (Voltage - dustCleanVoltage) / 0.005;
}

void Dust_Sensor::PrintSerial()
{
	Serial.print(" Raw Signal Value (0-1023):");
	Serial.print(Vo_value);
	Serial.print(" | Volatage:");
	Serial.print(Voltage);
	Serial.print(" | Dust Density:");
	Serial.print(dustDensity);
	Serial.print("[ug/m3]");
	Serial.println();
	Serial.println();
	Serial.println();
}

void Dust_Sensor::PrintLCD()
{
	LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
	lcd.begin(16, 2);
	lcd.clear();                                     // lcd의 화면을 지웁니다.
	lcd.setCursor(0, 0);
	lcd.print("Jimin's PM2.5");
	lcd.setCursor(0, 1);
	lcd.print(Voltage);
	lcd.print("V ");
	lcd.print(dustDensity);
	lcd.print("ug/m3");
}

void Dust_Sensor::Main_Logic()
{
	Computing_Mean();
	PrintSerial();
	PrintLCD();

	delay(500);
}