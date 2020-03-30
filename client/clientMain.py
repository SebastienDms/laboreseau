from client.GestionConnexionCl import Connexion
from client.Commands import Command
from client.Handshake import Handshake

connexion: Connexion = Connexion()
handshake: Handshake = Handshake(connexion)

commandeRecue: bytes
commandeEnvoyee: bytes = b''


def TraitementCommandeRecue():
	global commandeEnvoyee

	login: bytes
	mdp: bytes

	if commandeRecue == Command.ASKAUTH.value:
		login = input(">> Votre login : ").encode()
		mdp = input(">> Votre mot de passe : ").encode()
		commandeEnvoyee = Command.AUTH.value
		connexion.Envoie(commandeEnvoyee + " " + login + " " + mdp)
	elif choix == 1:
		commandeEnvoyee = Command.TIME.value
		connexion.Envoie(commandeEnvoyee)
	elif choix == 2:
		commandeEnvoyee = Command.DISCONNECT.value
		connexion.Envoie(commandeEnvoyee)
	elif choix == 3:
		commandeEnvoyee = Command.CLOSE.value
		connexion.Envoie(commandeEnvoyee)
	else:
		commandeEnvoyee = Command.UNK.value
		print(">> Votre choix n'est pas reconnu")


# Etablissement de la connexion
connexion.Envoie(Command.SYN.value)
while handshake.ack(connexion.Recoit()):
	print("Connexion au serveur en cours...")

print("Connexion avec le serveur établie")

# Authentification du client
connexion.Envoie(Command.AUTH.value)
while connexion.Recoit() != Command.FAIL.value:
	commandeRecue = connexion.Recoit()

	TraitementCommandeRecue()

# Menu utilisateur
while commandeEnvoyee != Command.CLOSE.value:
	print(">> Tapez")
	print(">> 1 pour connaitre l'heure")
	print(">> 2 pour fermer la session")
	print(">> 3 pour fermer la connexion")
	choix = input(">> Votre choix : ")

	TraitementCommandeRecue()

connexion.Close()
