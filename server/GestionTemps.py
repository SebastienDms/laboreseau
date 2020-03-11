import time


class Temps:
	@staticmethod
	def GetHeure() -> bytes:
		return time.strftime("H:%M:%S").encode()

	@staticmethod
	def GetDate() -> bytes:
		return time.strftime("%d/%m/%Y").encode()
