#include "Fan_Things.h"

Fan_Things::Fan_Things()
{
	pinMode(this->fan_pwm_port, OUTPUT);
	Serial.begin(9600);
}

void Fan_Things::Init()
{
	Serial.begin(9600);
	pinMode(this->fan_pwm_port, OUTPUT);
}

void Fan_Things::set_pwm(int pwm)
{
	this->pwm_value = pwm;
}

void Fan_Things::receive_data()
{

	if (Serial.available() > 0)
	{
		int current = 0;

		current = Serial.parseInt(); //string으로 받아야 int로 변환한다.

		if (current > 0 && current != this->pwm_value)
		{
			set_pwm(current);
			ACK = true;
		}
	}
	if(! ACK)
	{
		Serial.print("fan,");
		Serial.println("25.0");
	}
}

void Fan_Things::Main_Logic()
{
	receive_data();
	analogWrite(fan_pwm_port, pwm_value);
}