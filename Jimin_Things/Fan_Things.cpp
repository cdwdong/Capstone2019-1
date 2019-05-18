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
	pinMode(4, INPUT);
	digitalWrite(4, LOW);
}

void Fan_Things::set_pwm(int pwm)
{
	this->pwn = pwm;
}

void Fan_Things::receive_data()
{
	int current = 0;

	if (Serial.available() > 0)
	{
		current = Serial.parseInt();
		set_pwm(current);
	}
}

void Fan_Things::Main_Logic()
{
	receive_data();
	analogWrite(fan_pwm_port, pwn);
}