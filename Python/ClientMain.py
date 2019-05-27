import net.CommuHandler as CommuHandler
import asyncio
from Timing import *


def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj, globals())


async def eventHandle(reader, writer):

    flag = Timing.NONE

    def actionSelect(flag):
        if flag == Timing.SEND_ID:
            pass
        elif flag == Timing.SEND_CODE:
            pass
        elif flag == Timing.SEND_DATA:
            pass
        elif flag == Timing.NONE:
            pass

    while flag != Timing.ERROR:
        pass

    code = await reader.read()
    executeCode(code.decode())
    writer.close()
    await writer.wait_closed()

client = CommuHandler.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(eventHandle))