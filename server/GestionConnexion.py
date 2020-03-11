from socket import *


class Connexion:
	__serverPort = 12000
	__serverSocket = socket(AF_INET, SOCK_STREAM)
	__serverSocket.bind(('', __serverPort))
	__serverSocket.listen(1)

	__connectionSocket = None
	__clientAddress = None

	def __init__(self):
		self.__connectionSocket, self.__clientAddress = self.__serverSocket.accept()

	@staticmethod
	def ExtraitLogin(chaine: bytes) -> (bytes, bytes):
		return chaine[1], chaine[2]

	def GetIp(self):
		return self.__clientAddress[0]

	def Close(self):
		self.__connectionSocket.close()
