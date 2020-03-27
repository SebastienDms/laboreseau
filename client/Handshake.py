from .Commands import *
from .GestionConnexionCl import Connexion


class Handshake:
    __clientSocket: Connexion

    def __init__(self, socketInit: Connexion):
        __clientSocket = socketInit
        __clientSocket.Envoie(Command.SYN.value)

    def ack(self, rep: bytes):
        if rep == Command.SYNOK:
            self.__clientSocket.Envoie(Command.OK.value)
            return False
        elif rep == Command.OK:
            return True
        else:
            self.__clientSocket.Envoie(Command.UNK.value)
            return False