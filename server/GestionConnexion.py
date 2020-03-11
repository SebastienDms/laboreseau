from socket import *


class Connexion:
	__nombreListeners = 1
	__serverPort = 12000
	__serverSocket = socket(AF_INET, SOCK_STREAM)
	__serverSocket.bind(('', __serverPort))
	__serverSocket.listen(__nombreListeners)

	__connectionSocket = None
	__clientAddress = None

	def __init__(self):
		self.__connectionSocket, self.__clientAddress = self.__serverSocket.accept()

	def GetIp(self):
		return self.__clientAddress[0]

	def Close(self):
		self.__connectionSocket.close()

	def GetConnection(self) -> socket:
		return self.__connectionSocket

	def SetConnection(self):
		self.__connectionSocket, self.__clientAddress = self.__serverSocket.accept()

	def SetNombreListeners(self, nombre: int):
		self.__nombreListeners = nombre
		self.__connectionSocket.listen(nombre)

	def Envoie(self, message: bytes):
		self.__connectionSocket.send(message)

	def Recoit(self, tailleBuffer: int = 1024) -> bytes:
		return self.__connectionSocket.recv(tailleBuffer)
