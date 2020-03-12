from .Command import *
from .GestionConnexion import Connexion


class Handshake:
    __connectionSocket: Connexion

    def __init__(self, socketInit: Connexion):
        __connectionSocket = socketInit

    def conack(self, rep: bytes):
        if rep == Command.SYN:
            self.__connectionSocket.Envoie(Command.SYNOK.value)
            return False
        elif rep == Command.OK:
            return True
        else:
            self.__connectionSocket.Envoie(Command.UNK.value)
            return False
