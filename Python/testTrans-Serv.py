import CommuHandler
import asyncio

def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj)

async def eventHandle(reader, writer):
    length = await reader.read(100)
    #code = await reader.read(length.decode())
    #executeCode(code.decode())


server = CommuHandler.ServerHandler('127.0.0.1', 8888)
asyncio.run(server.start(eventHandle))
