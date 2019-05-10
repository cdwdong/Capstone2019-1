"""
2019-05-10

상속 클래스
ThingsInfo
ThingsSerial
CommuHandler

이것이 하나의 Things 클래스

"""

import ThingsInfo
import ThingsSerial as serial
import CommuHandler
import asyncio
from CommuHandler import ClientHandler
import ClientCommunication as tcp

class ThingsMain():
    
    ip = "52.78.166.156"
    port = 22
    
    def __init__(self):
        pass
        

    def Serial_Read_after_Trans_Server(self):
        arduino = serial.ThingsSerial("/dev/ttyUSB0", 9600)

        handle = ClientHandler(self.ip, self.port)
     
        while True:
             message = arduino.Serial_readline();

            if message:
                asyncio.run(tcp.tcp_echo_client(self.ip, self.port, message))
            
            
begin = ThingsMain()
begin.Serial_Read_after_Trans_Server()

