from socket import *
from typing import List

from server.GestionTemps import Temps
from server.Handshake import Handshake
from server.GestionSession import Session
from server.GestionLogin import Login
from server.Command import Command

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # nbr de connexion client

connectionSocket, clientAddress = serverSocket.accept()

log: Login = Login()
session: Session = Session.GetInstance()
handshake: Handshake = Handshake(connectionSocket)

while handshake.conack(connectionSocket.recv(1024)):
	serverSocket.listen(1)
	connectionSocket, clientAddress = serverSocket.accept()

if session.SessionExiste(clientAddress[0]):
	print('coucou')
else:
	connectionSocket.send(Command.ASKAUTH.value)
	rep: bytes = connectionSocket.recv(1024)
	rep2: List[bytes] = rep.split(b' ')
	if log.Log(rep2[0], rep2[1]):
		connectionSocket.send(Command.AUTHOK.value)
		session.CreerSession(clientAddress[0], rep2[0])
	else:
		connectionSocket.send(Command.FAIL.value)
