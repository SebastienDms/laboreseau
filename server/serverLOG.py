from typing import List

from server.Handshake import Handshake
from server.GestionSession import Session
from server.GestionLogin import Login
from server.Command import Command
from server.GestionConnexion import Connexion

connexion: Connexion = Connexion()
log: Login = Login.Instance()
session: Session = Session.Instance()
handshake: Handshake = Handshake(connexion.GetConnection())

while handshake.conack(connexion.Recoit()):
	connexion.SetNombreListeners(1)
	connexion.SetConnection()

if session.SessionExiste(connexion.GetIp()):
	print('coucou')
else:
	connexion.Envoie(Command.ASKAUTH.value)

	logs: List[bytes] = log.ExtraitLogin(connexion.Recoit())
	if log.Log(logs[Login.NAME], logs[Login.PWD]):
		connexion.Envoie(Command.AUTHOK.value)
		session.CreerSession(connexion.GetIp(), logs[Login.NAME])
	else:
		connexion.Envoie(Command.FAIL.value)
