from enum import Enum


class Command(Enum):
	AUTH = 1  # commande pour s'authentifier
	DISCONNECT = 2  # commande pour mettre fin à la session mais pas la connexion
	CLOSE = 3  # commande pour mettre fin à la connexion
	AUTHOK = 4  # connexion à la session réussie
	FAIL = 5  # connexion à la session ratée
	TIME = 6  # commande pour obtenir le temps
	SYN = "SYN" # demande de synchro du client (handshake)
	SYNOK = "SYNOK" # confirmation du serveur pour la dmd de synchro
	OK = "OK" # indique que le client en envie (ACK)

