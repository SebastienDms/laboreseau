from client.GestionConnexionCl import Connexion
from client.Commands import Command
from client.Handshake import Handshake

connexion: Connexion = Connexion()
handshake: Handshake = Handshake()

connexion.Envoie(Command.SYN.value)
while not Handshake.ack(connexion.Recoit()):
    input("Connexion au serveur en cours...")

input("Connexion avec le serveur établie")
connexion.Envoie(Command.AUTH.value)



clientSocket.close()