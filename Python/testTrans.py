import CommuHandler
import asyncio
import os

def openCode():
    with open("./test/code.txt") as f:
        return f.read()

async def EventHandle(reader, writer):
    code = openCode()
    if code == -1:
        return
    '''
    mystat = os.stat("./test/code.txt")
    print("mystat :", mystat)

    mysize = mystat.st_size
    print("mysize :", mysize)

    writer.write(str(mysize).encode())
    await writer.drain()
    '''

    writer.write(code.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

client = CommuHandler.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(EventHandle))
