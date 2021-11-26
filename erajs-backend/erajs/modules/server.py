from datetime import datetime, timedelta
from os.path import exists, splitext
from threading import Thread
from typing import Any, Callable, List, Literal, Optional

from fastapi import (Cookie, Depends, FastAPI, HTTPException, Request,
                     Response, WebSocket, status)
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from uvicorn import run
from yaml import safe_dump, safe_load


class Server:
    def start(self):
        pass

    def on(self, event: Literal['connect', 'data', 'close'], callback: Callable[[], Any]):
        pass

    def send_to(self, uid, data):
        pass


SECRET_KEY = ''
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
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
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class ClientManager:
    def new(self, addr):
        print('new')


cm = ClientManager()


class User(BaseModel):
    username: str
    nickname: str


def encrypt(password: str):
    encrypted_password = pwd_context.hash(password)
    return encrypted_password


def verify(password: str, encrypted_password: str):
    return pwd_context.verify(password, encrypted_password)


def valid_user(username: str, password: str):
    if username in user_db and verify(password, user_db[username]['encrypted_password']):
        return User(**user_db[username], username=username)
    return None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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
    oauth2_scheme = OAuth2PasswordBearer('/api/login')

    @app.post('/api/register', tags=['login'])
    async def register(form_data: OAuth2PasswordRequestForm = Depends()):
        # Check User
        user_data = user_db.get(form_data.username)
        if user_data:
            raise HTTPException(
                status_code=400, detail="User Already Exist")
        # Generate User
        user_db[form_data.username] = {
            'encrypted_password': encrypt(form_data.password),
            'nickname': ''
        }
        with open('user_db.yml', 'w')as f:
            safe_dump(user_db, f)
        # Generate Token
        return {
            'access_token': form_data.username,
            'token_type': 'bearer'
        }

    @app.post('/api/login', tags=['login'])
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        # Get User
        user = valid_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        # Generate Token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return {
            'access_token': access_token,
            'token_type': 'bearer'
        }
        #
        user_data = user_db.get(form_data.username)
        if not user_data:
            raise HTTPException(
                status_code=400, detail="Incorrect Username or Password")
        encrypted_password = encrypt(form_data.password)
        if not encrypted_password == user_data['encrypted_password']:
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
    global user_db
    global SECRET_KEY
    if exists('SECRET_KEY'):
        with open('SECRET_KEY') as f:
            SECRET_KEY = f.read()
    open('user_db.yml', 'a')
    with open('user_db.yml') as f:
        user_db = safe_load(f)
        if not user_db:
            user_db = {}
    t = Thread(target=server, kwargs={
               'host': host, 'port': port})
    print('http://{}:{}'.format(host, port))
    t.start()


def send_to():
    pass
