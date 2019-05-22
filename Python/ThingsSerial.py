"""
2019-05-04

아두이노 시리얼 읽기

작성자: 서지민

"""
import ThingsInfo
import serial

class ThingsSerial():

    #port_number = "/dev/ttyUSB0" #linux
    port_number = "COM4"  #windows
    baudrate = 9600

    #시리얼 객체
    things_serial = 0

    #Que buffer
    Que_buffer = {}

    #buffer pointer
    buffer_pointer = 0;

    # 시리얼 객체를 생성
    def __init__(self, port_number, baudrate):
        self.port_number = port_number
        self.baudrate = baudrate

        self.things_serial = serial.Serial(port_number, baudrate)

    def serial_readline(self):
        if self.things_serial.readable():
            res = self.things_serial.readline()
            #self.Que_buffer.append(res)
            self.buffer_pointer = self.buffer_pointer + 1
        return res


begin = ThingsSerial("COM11", 9600)

while True:
    data = begin.serial_readline()
    if data:
        print(data)
