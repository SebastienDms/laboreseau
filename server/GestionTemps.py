import time


class Temps:
	@staticmethod
	def GetHeure() -> str:
		return time.strftime("H:%M:%S").encode()

	@staticmethod
	def GetDate() -> str:
		return time.strftime("%d/%m/%Y").encode()
