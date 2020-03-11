class Session:
	__instance = None

	__listeSession = {}

	@staticmethod
	def GetInstance():
		if Session.__instance is None:
			Session()
		return Session.__instance

	def __init__(self):
		if Session.__instance is None:
			Session.__instance = self

	def SessionExiste(self, adresseIp) -> bool:
		for ip in self.__listeSession:
			if self.__listeSession[ip] == adresseIp:
				return True

		return False

	def CreerSession(self, adresseIp, login: str):
		self.__listeSession[adresseIp] = login
