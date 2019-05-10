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
import sys
import asyncio
from CommuHandler import ClientHandler


class ThingsMain(ThingsInfo, ThingsSerial, CommuHandler):

    def Serial_Read_after_Trans_Server(self):
        """
        #begin = ThingsSerial("COM4", 9600);
        #begin.serial_read()
        """

        arduino = ThingsSerial("/dev/ttyUSB0", 9600);

        nethandler = CommuHandler();
        net = nethandler.ClientHandler("52.78.166.156", 22);

        while True:
            message = arduino.Serial_readline();

            asyncio.run(ClientHandler.tcp_echo_client(message))