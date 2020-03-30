from socket import *


class Connexion:
	__nombreListeners = 1
	__serverPort = 12000
	__serverSocket = socket(AF_INET, SOCK_STREAM)
	__serverSocket.bind(('', __serverPort))
	__serverSocket.listen(__nombreListeners)

	__connectionSocket = None
	__clientAddress = None

	__state: bool = False

	def __init__(self):
		self.__connectionSocket, self.__clientAddress = self.__serverSocket.accept()
		self.__state = True

	def GetIp(self):
		return self.__clientAddress[0]

	def Close(self):
		if self.__state:
			self.__connectionSocket.close()
			self.__state = False

	def GetConnection(self) -> socket:
		return self.__connectionSocket

	def SetConnection(self):
		self.__connectionSocket, self.__clientAddress = self.__serverSocket.accept()

	def SetNombreListeners(self, nombre: int):
		self.__nombreListeners = nombre
		self.__connectionSocket.listen(nombre)

	def Envoie(self, message: bytes):
		print("Envoie " + message.decode())
		self.__connectionSocket.send(message)

	def Recoit(self, tailleBuffer: int = 1024) -> bytes:
		recoit: bytes = self.__connectionSocket.recv(tailleBuffer)
		print("Recoit " + recoit.decode())
		return recoit

	def State(self) -> bool:
		return self.__state
