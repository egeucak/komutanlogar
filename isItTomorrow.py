from datetime import datetime
from datetime import timedelta


class IsItTomorrow:

	logLoc = ""
	def __init__(self, logLoc):
		self.logLoc = logLoc

	def getLastLine(self):
		f = open(self.logLoc, "rb")
		f.seek(-27,2)
		lastline = f.readline()[:-1]
		f.close()
		return str(lastline)[2:-1]

	def isIt(self):
		itIs = False
		lastLine = self.getLastLine()
		yesterday = datetime.strptime(lastLine, '%Y-%m-%d %H:%M:%S.%f')
		today = datetime.now()
		delta = timedelta(days = +1)
		if (yesterday + delta < today and datetime.now().hour > 12):
			itIs = True
		return itIs
