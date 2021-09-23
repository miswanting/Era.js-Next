from os.path import exists, splitext
from threading import Thread
from typing import List, Optional

from fastapi import FastAPI, Request, Response, WebSocket, Cookie
from fastapi.responses import HTMLResponse
from uvicorn import run

mime = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.ttf': 'font/ttf',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
}


class ClientManager:
    def new(self, addr):
        print('new')


cm = ClientManager()


def server(host: str = 'localhost', port: int = 11994):
    app = FastAPI()

    @app.websocket('/ws')
    async def connect(ws: WebSocket):
        # Waiting for a Connection.
        await ws.accept()
        # Connection Accepted.
        # New a
        # print(dir(request))
        cm.new()
        while True:
            data = await ws.receive_text()
            recv(data)
            # await ws.send_text(data)

    @app.get('/assets{file_path:path}')
    def assets(file_path):
        path = '../erajs-frontend-web/dist/assets{}'.format(file_path)
        if exists(path):
            ext = splitext(path)[1]
            m = mime[ext]
            with open(path, 'rb') as file:
                return Response(file.read(), media_type=m)

    @app.get('{file_path:path}')
    def root(file_path, uid: Optional[str] = Cookie(None)):
        print(uid)
        with open('../erajs-frontend-web/dist/index.html') as file:
            return HTMLResponse(file.read())
    run(app, host=host, port=port, log_level='error')


def recv(data):
    print(f'Recv: {data}')


def start(host: str = 'localhost', port: int = 11994):
    t = Thread(target=server, kwargs={'host': host, 'port': port})
    t.start()


def send_to():
    pass
