from .Command import *
from .serverLOG import connectionSocket


class Handshake:

    def conack(self, rep: bytes):
        if rep == Command.SYN:
            connectionSocket.send(Command.SYNOK)
            return False
        elif rep == Command.OK:
            return True
        else:
            connectionSocket.send(Command.UNK)
            return False
