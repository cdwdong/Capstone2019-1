"""
2019-05-04

아두이노 시리얼 읽기

작성자: 서지민

"""

import serial

class ThingsSerial:

    port_number = "COM4"
    baudrate = 9600

    things_serial = 0

    # 시리얼 객체를 생성
    def __init__(self, port_number, baudrate):
        self.port_number = port_number
        self.baudrate = baudrate

        self.things_serial = serial.Serial(port_number, baudrate)


    def Serial_readline(self):
        if self.things_serial.readable():
            res = self.things_serial.readline()
        return res

    # 시리얼 객체를 받아서 지속적으로 출력
    def serial_read(self):
        while True:
            res = self.Serial_readline()
            print(res.decode()[:len(res) - 1])


#begin = ThingsSerial("COM4", 9600);
#begin.serial_read()