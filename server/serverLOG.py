from typing import List

from server.Handshake import Handshake
from server.GestionSession import Session
from server.GestionLogin import Login
from server.Command import Command
from server.GestionConnexion import Connexion
from server.GestionTemps import Temps

connexion: Connexion = Connexion()
log: Login = Login.Instance()
session: Session = Session.Instance()
handshake: Handshake = Handshake(connexion)

commandeRecue: bytes


def FuncLogin():
	if session.SessionExiste(connexion.GetIp()):  # si la session est déjà connue
		connexion.Envoie(Command.AUTHOK.value)  # on informe le client qu'il est déjà authentifié
	else:  # sinon c'est une nouvelle session
		connexion.Envoie(Command.ASKAUTH.value)  # on demande une authentification

		logs: List[bytes] = log.ExtraitLogin(connexion.Recoit())  # récupère les logs utilisateur/mdp
		print(logs)
		print(Login.NAME)
		if log.Log(logs[Login.NAME], logs[Login.PWD]):  # si les logs existent
			connexion.Envoie(Command.AUTHOK.value)  # informe le client qu'il est connecté
			session.CreerSession(connexion.GetIp(), logs[Login.NAME])  # réalise la connexion
		else:
			connexion.Envoie(Command.FAIL.value)  # si les logs n'existent pas on informe le client


def TraitementCommandeRecue():
	if commandeRecue == Command.AUTH.value:  # si le client demande de s'authentifier
		FuncLogin()
	elif commandeRecue == Command.TIME.value:  # si le client demander l'heure du serveur
		connexion.Envoie(Temps.GetHeure())
	elif commandeRecue == Command.DISCONNECT.value:  # si le client demande de se déconnecter
		session.Deconnexion(connexion.GetIp())
		connexion.Envoie(Command.DISOK.value)
	elif commandeRecue == Command.CLOSE.value:  # si le client demande à fermer la connexion
		connexion.Envoie(Command.CLOSEOK.value)
		connexion.Close()
	else:  # la commande reçue n'est pas connue
		connexion.Envoie(Command.UNK.value)


# Etablissement de la connexion
while handshake.conack(connexion.Recoit()):
	pass

while connexion.State():
	print(1)
	commandeRecue = connexion.Recoit()  # attend la prochaine commande
	print(2)
	TraitementCommandeRecue()
	print(3)
