from .modules import server
from .modules.server import Server


def init():
    server.start(port=80)
    s = Server()
    s.start()
    s.on('data')
