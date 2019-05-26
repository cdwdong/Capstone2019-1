import lib.CommuHandler as CommuHandler
import asyncio

def openCode():
    with open("./script/Test-Serial-Script.py") as f:
        return f.read()

async def EventHandle(reader, writer):
    code = openCode()
    if code == -1:
        return
    writer.write(code.encode())
    await writer.drain()
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

server = CommuHandler.ServerHandler('172.26.2.32', 8888)
asyncio.run(server.start(EventHandle))
