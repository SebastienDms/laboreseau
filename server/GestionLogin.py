class Login():
	__listeLogin = {
		"root": "root",
		"seb": "star"
	}

	def GetLogin(self, motDePasse):
		loginRetour = "NULL"

		for login in self.__listeLogin:
			if self.__listeLogin[login] == motDePasse:
				loginRetour = login

		return loginRetour
