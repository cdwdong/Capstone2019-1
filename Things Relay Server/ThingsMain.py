"""
2019-05-10

상속 클래스
ThingsInfo
ThingsSerial
CommuHandler

이것이 하나의 Things 클래스

"""

import ThingsInfo
import ThingsSerial
import CommuHandler
import asyncio
from CommuHandler import ClientHandler


class ThingsMain(ThingsInfo, ThingsSerial, CommuHandler):

    def Serial_Read_after_Trans_Server(self):


        arduino = ThingsSerial("/dev/ttyUSB0", 9600);

        ip = "52.78.166.156"
        port = 22

        while True:
            message = arduino.Serial_readline();

            asyncio.run(ClientHandler.tcp_echo_client(ip, port, message))

