from socket import *


class Connexion:
	__serveurName: str
	__serverPort: int
	__clientSocket: socket

	__state: bool = False

	def __init__(self):
		self.__serveurName = "127.0.0.1"
		self.__serverPort = 12000
		self.__clientSocket = socket(AF_INET, SOCK_STREAM)
		self.__clientSocket.connect((self.__serveurName, self.__serverPort))
		self.__state = True

	def Close(self):
		if self.__state:
			self.__clientSocket.close()
			self.__state = False

	def GetConnection(self) -> socket:
		return self.__clientSocket

	def Envoie(self, message: bytes):
		print("Envoie " + message.decode())
		self.__clientSocket.send(message)

	def Recoit(self, tailleBuffer: int = 1024) -> bytes:
		recoit: bytes = self.__clientSocket.recv(tailleBuffer)
		print("Recoit " + recoit.decode())
		return recoit
