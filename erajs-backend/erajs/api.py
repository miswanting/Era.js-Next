from .modules import server


def init():
    server.start(port=80)
