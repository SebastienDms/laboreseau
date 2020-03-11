class Login:
	__listeLogin = {
		"root": "root",
		"seb": "star"
	}

	def Log(self, motDePasse) -> bool:
		for login in self.__listeLogin:
			if self.__listeLogin[login] == motDePasse:
				return True

		return False
