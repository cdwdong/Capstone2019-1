import ThingsInfo
import ThingsSerial as serial

import sys
import asyncio
from CommuHandler import ClientHandler
'''
async def tcp_echo_client(ip, port, message):
    reader, writer = await asyncio.open_connection(
        ip, port)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
'''

#asyncio.run(tcp_echo_client('Hello World!'))
async def tcp_echo_client2(reader, writer):
    message = 'This is Test, jimin'

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

async def callbackTest(reader, writer):

    arduino = serial.ThingsSerial("/dev/ttyUSB0", 9600)

    while True:
        message = arduino.Serial_readline()
        writer.write(message.encode())

##############################################################
ip = "52.78.166.156"
port = 8888
handle = ClientHandler(ip, port)
asyncio.run(handle.start(callbackTest))
