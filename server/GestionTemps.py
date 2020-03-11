import time


class Temps:
	def GetHeure(self):
		time.strftime("%H:%M:%S")

	def GetDate(self):
		time.strftime("%d/%m/%Y")
