from enum import Enum


class Command(Enum):
	AUTH = b'AUTH'  # commande pour s'authentifier
	DISCONNECT = b'DISCONNECT'  # commande pour mettre fin à la session mais pas la connexion
	CLOSE = b'CLOSE'  # commande pour mettre fin à la connexion
	AUTHOK = b'AUTHOK'  # connexion à la session réussie
	FAIL = b'FAIL'  # connexion à la login/session ratée
	TIME = b'TIME'  # commande pour obtenir le temps
	ASKAUTH = b'ASKAUTH' # demande au client de s'authentifier
	SYN = b'SYN' # demande de synchro du client (handshake)
	SYNOK = b'SYNOK' # confirmation du serveur pour la dmd de synchro
	OK = b'OK' # indique que le client en envie (ACK)
	UNK = b'BADC' # indique que la commande n'est pas reconnue


