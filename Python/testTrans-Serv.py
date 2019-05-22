from lib.CommuHandler import CommuHandler
import asyncio

def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj)

async def eventHandle(reader, writer):
    code = await reader.read()
    executeCode(code.decode())
    writer.close()
    await writer.wait_closed()

server = CommuHandler.ServerHandler('172.26.2.32', 8888)
asyncio.run(server.start(eventHandle))
