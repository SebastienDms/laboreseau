from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')
message: bytes
while 1:
	connectionSocket, clientAddress = serverSocket.accept()

	reponse = bytes("Bonjour client " + clientAddress[0] + " sur le port " + str(clientAddress[1]), 'utf-8')
	connectionSocket.send(reponse)

	commande: bytes = connectionSocket.recv(1024)  # nombre de bits à lire dans la mémoire tampon
	if commande.decode().upper() == "LOGIN":
		reponse = bytes("Votre login : ", 'utf-8')
		connectionSocket.send(reponse)

		login: bytes = connectionSocket.recv(1024)

		if login.decode() == 'root':
			reponse = bytes("Bonjour Admin", 'utf-8')
		elif login.decode() == "seb":
			reponse = bytes("Bonjour Seb", 'utf-8')
		else:
			reponse = bytes("Bonjour Inconnu", 'utf-8')
	elif commande.decode().upper() == "TIME":
		reponse = bytes("Il est " + time.strftime("%H:%M:%S"), 'utf-8')
	else:
		reponse = bytes("Commande inconnue", 'utf-8')

	connectionSocket.send(reponse)
	print(reponse.decode())

	reponse = bytes("CLOSE", 'utf-8')
	connectionSocket.send(reponse)  # sendto envoie et ferme la connexion
	connectionSocket.close()
