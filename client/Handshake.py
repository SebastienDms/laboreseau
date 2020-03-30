from .Commands import *
from .GestionConnexionCl import Connexion


class Handshake:
	__clientSocket: Connexion

	def __init__(self, socketInit: Connexion):
		self.__clientSocket = socketInit

	def ack(self, rep: bytes):
		# print("ACK " + rep.decode())
		if rep == Command.SYNOK.value:
			self.__clientSocket.Envoie(Command.OK.value)
			return True
		elif rep == Command.OK.value:
			return False
		else:
			self.__clientSocket.Envoie(Command.UNK.value)
			return True
