from enum import Enum, auto


class AutoName(Enum):
	def _generate_next_value_(name, start, count, last_values):
		return str(name).encode()


class Command(AutoName):
	AUTH = auto()  # commande pour s'authentifier
	DISCONNECT = auto()  # commande pour mettre fin à la session mais pas la connexion
	CLOSE = auto()  # commande pour mettre fin à la connexion
	AUTHOK = auto()  # connexion à la session réussie
	FAIL = auto()  # connexion à la login/session ratée
	TIME = auto()  # commande pour obtenir le temps
	ASKAUTH = auto()  # demande au client de s'authentifier
	SYN = auto()  # demande de synchro du client (handshake)
	SYNOK = auto()  # confirmation du serveur pour la dmd de synchro
	OK = auto()  # indique que le client en envie (ACK)
	UNK = auto()  # indique que la commande n'est pas reconnue


