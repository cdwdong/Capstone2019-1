import lib.CommuHandler as CommuHandler
import asyncio
from Timing import *


def openCode():
    with open("./script/Test-Serial-Script.py") as f:
        return f.read()


async def eventHandle(reader, writer):

    flag = Timing.NONE

    def actionSelect(flag):
        if flag == Timing.SEND_ID:
            pass
        elif flag == Timing.SEND_CODE:
            pass
        elif flag == Timing.SEND_DATA:
            pass
        elif flag == Timing.ETC:
            pass

    while flag != Timing.ERROR:
        pass

    code = openCode()
    if code == -1:
        return
    writer.write(code.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

server = CommuHandler.ServerHandler('172.26.2.32', 8888)
asyncio.run(server.start(eventHandle))
