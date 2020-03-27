from client.GestionConnexionCl import Connexion
from client.Commands import Command
from client.Handshake import Handshake

connexion: Connexion = Connexion()
handshake: Handshake = Handshake()

commandeRecue: bytes
commandeEnvoyee: bytes
login: bytes
mdp: bytes

def TraitementCommandeRecue():
    if commandeRecue == Command.ASKAUTH.value:
        login = input(">> Votre login : ")
        mdp = input(">> Votre mot de passe : ")
        connexion.Envoie(Command.AUTH+login+mdp)
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
        print(">> Votre choix n'est pas reconnu")


# Etablissement de la connexion
connexion.Envoie(Command.SYN.value)
while Handshake.ack(connexion.Recoit()):
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
    print(">> 1 pour connaitre l\'heure")
    print(">> 2 pour fermer la session")
    print(">> 3 pour fermer la connexion")
    choix = input(">> Votre choix : ")

    TraitementCommandeRecue()


clientSocket.close()