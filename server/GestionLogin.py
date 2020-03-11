class Login:
	__listeLogin = {
		b'root': b'root',
		b'seb': b'star'
	}

	def Log(self, motDePasse: bytes) -> bool:
		for login in self.__listeLogin:
			if self.__listeLogin[login] == motDePasse:
				return True

		return False
