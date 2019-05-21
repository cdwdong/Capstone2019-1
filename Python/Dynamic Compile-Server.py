import CommuHandler
import asyncio

def executeCode(code):
    code_obj = compile(code,"<string>", 'exec')
    exec(code_obj)

async def eventHandle(reader, writer):

    while True:
        """
        file_size_bytes = await reader.read(100)

        file_size = int.from_bytes(file_size_bytes, 'big')

        writer.write(file_size_bytes)
        await writer.drain()
        """
        code = await reader.read(1024)
        if code: # 파일크기가 0 보다 커야 함
            print("dynamic code -> ", code)
            executeCode(code.decode())


server = CommuHandler.ServerHandler('127.0.0.1', 8888)
asyncio.run(server.start(eventHandle))