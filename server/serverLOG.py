from socket import *
from .GestionTemps import Temps
from .Handshake import *
from .GestionSession import *
from .GestionLogin import *
from .Command import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1) # nbr de connexion client

connectionSocket, clientAddress = serverSocket.accept()

while Handshake.conack(connectionSocket.recv(1024)):
    serverSocket.listen(1)
    connectionSocket, clientAddress = serverSocket.accept()

if Session.SessionExiste(clientAddress[0]):

else:
    connectionSocket.send(Command.ASKAUTH)
    rep = connectionSocket.recv(1024)
    rep = rep[-2:]
    if Login.Log(rep[0], rep[1]):
       connectionSocket.send(Command.AUTHOK)
       Session.CreerSession(clientAddress[0], rep[0])
    else:
        connectionSocket.send(Command.FAIL)
    

