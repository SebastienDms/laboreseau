class Login:
	__listeLogin = {
		b'root': b'root',
		b'seb': b'star'
	}

	def Log(self, log: bytes, motDePasse: bytes) -> bool:
		if log in self.__listeLogin:
			if self.__listeLogin[log] == motDePasse:
				return True

		return False
