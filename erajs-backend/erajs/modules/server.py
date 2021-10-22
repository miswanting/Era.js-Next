from os.path import exists, splitext
from threading import Thread
from typing import List, Optional

from fastapi import (Cookie, Depends, FastAPI, HTTPException, Request,
                     Response, WebSocket)
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from uvicorn import run
from yaml import safe_dump, safe_load

mime = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.ttf': 'font/ttf',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
}
tags = [
    {
        'name': 'login',
        'description': 'User Login Logic'
    }
]
user_db = {}


class ClientManager:
    def new(self, addr):
        print('new')


cm = ClientManager()


def server(host: str = 'localhost', port: int = 11994):
    app = FastAPI(
        title="Era.js Game Server",
        description='Server for Era.js Game Engine.',
        version="0.1.0",
        terms_of_service="",
        contact={
            "name": "Miswanting",
            "url": "http://example.com",
            "email": "ihex@foxmail.com",
        },
        license_info={
            "name": "GPL-3.0+",
            "url": "http://example.com",
        },
        openapi_tags=tags
    )
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

    @app.post('/api/register', tags=['login'])
    async def register(form_data: OAuth2PasswordRequestForm = Depends()):
        user_data = user_db.get(form_data.username)
        if user_data:
            raise HTTPException(
                status_code=400, detail="User Already Exist")
        user_db[form_data.username] = {
            'encrypted_password': form_data.password
        }
        with open('user_db.yml', 'w')as f:
            safe_dump(user_db, f)
        return {
            'access_token': form_data.username,
            'token_type': 'bearer'
        }

    @app.post('/api/login', tags=['login'])
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        user_data = user_db.get(form_data.username)
        if not user_data:
            raise HTTPException(
                status_code=400, detail="Incorrect Username or Password")
        encrypted_password = form_data.password
        if not encrypted_password == encrypted_password:
            raise HTTPException(
                status_code=400, detail="Incorrect Username or Password")
        return {
            'access_token': form_data.username,
            'token_type': 'bearer'
        }

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

    @app.get('/assets/{file_path:path}')
    def assets(file_path):
        path = 'erajs/www/assets/{}'.format(file_path)
        if exists(path):
            ext = splitext(path)[1]
            m = mime[ext]
            with open(path, 'rb') as file:
                return Response(file.read(), media_type=m)

    @app.get('{file_path:path}')
    def root(file_path, uid: Optional[str] = Cookie(None)):
        print(uid)
        with open('erajs/www/index.html') as file:
            return HTMLResponse(file.read())
    run(app, host=host, port=port, log_level='error')


def recv(data):
    print(f'Recv: {data}')


def start(host: str = 'localhost', port: int = 11994):
    open('user_db.yml', 'r')
    with open('user_db.yml')as f:
        user_db = safe_load(f)
        if not user_db:
            user_db = {}
    t = Thread(target=server, kwargs={'host': host, 'port': port})
    print('http://{}:{}'.format(host, port))
    t.start()


def send_to():
    pass
