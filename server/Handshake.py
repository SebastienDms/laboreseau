from socket import socket
from .Command import *


class Handshake:
    __connectionSocket: socket

    def __init__(self, socketInit: socket):
        __connectionSocket = socketInit

    def conack(self, rep: bytes):
        if rep == Command.SYN:
            self.__connectionSocket.send(Command.SYNOK.value)
            return False
        elif rep == Command.OK:
            return True
        else:
            self.__connectionSocket.send(Command.UNK.value)
            return False
