from socket import *
from .GestionTemps import Temps
from .Handshake import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

connectionSocket, clientAddress = serverSocket.accept()
Handshake.conack(connectionSocket.recv(1024))

while Handshake.conack(connectionSocket.recv(1024)):
    serverSocket.listen(1)
    connectionSocket, clientAddress = serverSocket.accept()


