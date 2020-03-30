from client.GestionConnexionCl import Connexion
from client.Commands import Command
from client.Handshake import Handshake

connexion: Connexion = Connexion()
handshake: Handshake = Handshake(connexion)

commandeRecue: bytes
commandeEnvoyee: bytes = b''


def Authentification():
	global commandeRecue

	# Authentification du client
	connexion.Envoie(Command.AUTH.value)
	commandeRecue = connexion.Recoit()
	while commandeRecue != Command.AUTHOK.value:
		TraitementCommandeRecue("0")

		commandeRecue = connexion.Recoit()


def TraitementCommandeRecue(choix: str):
	global commandeEnvoyee

	login: str
	mdp: str

	resultat: bytes

	if commandeRecue == Command.ASKAUTH.value or choix == "0":
		login = input(">> Votre login : ")
		mdp = input(">> Votre mot de passe : ")
		commandeEnvoyee = Command.AUTH.value
		connexion.Envoie(commandeEnvoyee + (" " + login + " " + mdp).encode())
	elif choix == "1":
		commandeEnvoyee = Command.TIME.value
		connexion.Envoie(commandeEnvoyee)

		resultat = connexion.Recoit()
		print("L'heure du serveur est " + resultat.decode())
	elif choix == "2":
		commandeEnvoyee = Command.DISCONNECT.value
		connexion.Envoie(commandeEnvoyee)

		if connexion.Recoit() == Command.DISOK.value:
			print("Déconnexion effectuée avec succès")
			Authentification()
		else:
			print("Erreur lors de la déconnexion")
	elif choix == "3":
		commandeEnvoyee = Command.CLOSE.value
		connexion.Envoie(commandeEnvoyee)

		if connexion.Recoit() == Command.CLOSEOK.value:
			print("Connexion fermée")
			connexion.Close()
		else:
			print("Erreur lors de la fermeture de connexion")
	else:
		commandeEnvoyee = Command.UNK.value
		print(">> Votre choix n'est pas reconnu")


# Etablissement de la connexion
connexion.Envoie(Command.SYN.value)
while handshake.ack(connexion.Recoit()):
	print("Connexion au serveur en cours...")

print("Connexion avec le serveur établie")

Authentification()

# Menu utilisateur
while commandeEnvoyee != Command.CLOSE.value:
	print(">> Tapez")
	print(">> 1 pour connaitre l'heure")
	print(">> 2 pour fermer la session")
	print(">> 3 pour fermer la connexion")
	choixNumero = input(">> Votre choix : ")

	TraitementCommandeRecue(choixNumero)


connexion.Close()
