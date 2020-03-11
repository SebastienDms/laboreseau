import time


class Temps:
	@staticmethod
	def GetHeure():
		return time.strftime("%H:%M:%S")

	@staticmethod
	def GetDate():
		return time.strftime("%d/%m/%Y")
