class Lines:
	lineLoc = ""
	def __init__ (self, loc):
		Lines.lineLoc = loc
		try:										#Let's import random library in a class. Because why not?
			import random
		except ImportError:
			self.random = None
		else:
			self.random = random

	def getLine(self):
		file = open(Lines.lineLoc, "r", encoding='cp1254')
		garavel = file.read().splitlines()
		file.close()
		x = 0
		while (x == 0):
			secilen = self.random.choice(garavel).strip()
			if (len(secilen) > 3):
				x = 1
		if "=" in secilen:
			secilen = secilen.split("=")[1]
		return (secilen)
