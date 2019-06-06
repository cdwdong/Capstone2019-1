import asyncio
import inspect

class CommuHandler:
    
    def __init__(self):
        pass

    async def start(self):
        pass

    async def handle(self, reader, writer):
        pass


# 서버 생성 클래스
class ServerHandler(CommuHandler):
    def __init__(self, ipaddr, port, **kwargs):
        CommuHandler.__init__(self)
        self.ipaddr, self.port = ipaddr, port
        self.kwargs = kwargs

# asyncio.run(객체명.start(callback)) 형식으로 사용
    async def start(self, callback=None):
        server = await asyncio.start_server(callback, host=self.ipaddr, port=self.port, **self.kwargs)

        async with server:
            await server.serve_forever()


# 클라이언트 생성 클래스
class ClientHandler(CommuHandler):
    def __init__(self, ipaddr, port, **kwargs):
        CommuHandler.__init__(self)
        self.ipaddr, self.port = ipaddr, port
        self.kwargs = kwargs

    async def start(self, callback):
        reader, writer = await asyncio.open_connection(host=self.ipaddr, port=self.port, **self.kwargs)
        if inspect.iscoroutinefunction(callback):
            await callback(reader, writer)
        else:
            callback(reader, writer)
