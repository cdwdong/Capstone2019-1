import lib.CommuHandler as CommuHandler
import asyncio
import Timing

def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj, globals())

async def eventHandle(reader, writer):
    code = await reader.read()
    executeCode(code.decode())
    writer.close()
    await writer.wait_closed()

def actionSelect(flag):
    if flag == Timing.Timing.SEND_ID:
        pass
    elif flag == Timing.Timing.SEND_CODE:
        pass
    elif flag == Timing.Timing.SEND_DATA:
        pass
    elif flag == Timing.Timing.ETC:
        pass

client = CommuHandler.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(eventHandle))