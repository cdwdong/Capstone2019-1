import CommuHandler
import asyncio
import os

def openCode():
    with open("./test/code.txt") as f:
        return f.read()
    return -1
async def EventHandle(reader, writer):
    code = openCode()
    if code == -1:
        return
    mystat = os.stat("./test/code.txt")
    print("mystat :", mystat)

    mysize = mystat.st_size
    print("mysize :", mysize)

    await writer.write(str(mysize).encode())
    await writer.write(code.encode())

client = CommuHandler.ClientHandler('127.0.0.1', 8888)
asyncio.run(client.start(EventHandle))
