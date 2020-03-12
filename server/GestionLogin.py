from typing import List


class Login:
	__instance = None

	__listeLogin = {
		b'root': b'root',
		b'seb': b'star'
	}

	NAME = 0
	PWD = 1

	@staticmethod
	def Instance():
		if Login.__instance is None:
			Login()
		return Login.__instance

	def __init__(self):
		if Login.__instance is None:
			Login.__instance = self

	def Log(self, log: bytes, motDePasse: bytes) -> bool:
		if log in self.__listeLogin:
			if self.__listeLogin[log] == motDePasse:
				return True

		return False

	@staticmethod
	def ExtraitLogin(chaine: bytes) -> (bytes, bytes):
		logs: List[bytes] = chaine.split(b' ')
		return logs[1], logs[2]
