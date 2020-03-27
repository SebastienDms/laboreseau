from .Command import *
from .GestionConnexion import Connexion


class Handshake:
	__connectionSocket: Connexion

	def __init__(self, socketInit: Connexion):
		self.__connectionSocket = socketInit

	def conack(self, rep: bytes):
		if rep == Command.SYN.value:
			self.__connectionSocket.Envoie(Command.SYNOK.value)
			return False
		elif rep == Command.OK.value:
			self.__connectionSocket.Envoie(Command.OK.value)
			return True
		else:
			self.__connectionSocket.Envoie(Command.UNK.value)
			return False
