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

    mysize = mystat.st_size # int로 반환
    print("mysize :", mysize)

    writer.write(code.encode())

    """
        while True:
        writer.write(mysize_str)
        await writer.drain()

        file_size_bytes = await reader.read(100)

        print("Client file_size: ", mysize, " Server file_size: ", file_size_bytes)

        if file_size_bytes == mysize_str:
            print("Client->Server code >",code)
            writer.write(code.encode())
            await writer.drain()
    """


client = CommuHandler.ClientHandler('127.0.0.1', 8888)
asyncio.run(client.start(EventHandle))