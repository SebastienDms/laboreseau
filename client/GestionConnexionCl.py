from socket import *


class Connexion:
    __serveurName: str
    __serverPort: int
    __clientSocket: socket

    def init(self):
        self.__serveurName = "0.0.0.0"
        self.__serverPort = 12000
        self.__clientSocket = socket(AF_INET, SOCK_STREAM)
        self.__clientSocket.connect((self.__serveurName, self.__serverPort))

    def Close(self):
        self.__clientSocket.close()

    def GetConnection(self) -> socket:
        return self.__connectionSocket

    def Envoie(self, message: bytes):
        self.__clientSocket.send(message)

    def Recoit(self, tailleBuffer: int = 1024) -> bytes:
        return self.__clientSocket.recv(tailleBuffer)