/*
2019-05-18

Fan pwm 제어

작성자 서지민

*/




#ifndef Fan_h
#define Fan_h

#include <stdio.h>
#include <time.h>

#include <Arduino.h>

class Fan_Things
{
public:
	const int fan_pwm_port = 3;
	int pwm_value = 4;

	Fan_Things();
	void Init();
	void receive_data();
	void set_pwm(int pwm);
	void Main_Logic();

};

#endif