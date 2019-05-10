import sys
import asyncio
from CommuHandler import ClientHandler

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()


#asyncio.run(tcp_echo_client('Hello World!'))
async def tcp_echo_client2(reader, writer):
    message = '안녕 복스'

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

handle = ClientHandler(str(sys.argv[1]), int(sys.argv[2]))
asyncio.run(handle.start(tcp_echo_client2))