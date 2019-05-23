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

server = CommuHandler.ServerHandler('172.26.2.32', 8888)
asyncio.run(server.start(EventHandle))
