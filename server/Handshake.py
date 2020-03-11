from socket import *
from .Command import *

class Handshake:

    def conack(self, rep: bytes):
        if rep == Command.SYN.decode():
            connectionSocket.send(bytes(Command.SYNOK))
            return False
        elif rep == Command.OK.decode():
            return True
        else:
            return False