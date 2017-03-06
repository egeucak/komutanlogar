from Lines import Lines
from Tweet import Tweet
from SameTweetException import SameTweetException
from isItTomorrow import IsItTomorrow
import time, datetime

def saveToLog(loc):
	logLoc = loc
	log = open(logLoc, "a")
	log.write(str(datetime.datetime.now())+"\n")
	log.close()
	return ()

def main():
	keysLoc = "keys.txt"
	linesLoc = "adim garavel.txt"
	timeLogLoc = "timeLog.txt"
	tweet1 = Tweet()
	lines1 = Lines(linesLoc)
	checker = IsItTomorrow(timeLogLoc)
	api = tweet1.get_api(keysLoc)
	while True:
		if (checker.isIt()):
			try:
				message = lines1.getLine()
				print(message)
				tweet1.postTweet(message, api)
				saveToLog(timeLogLoc)
			except SameTweetException:
				tweet1.postTweet(lines1.getLine(), api)
			time.sleep(300)

if __name__ == "__main__":
	try:
		main()
	except Exception:  #HA HA YOU CAN'T ESCAPE, EXCEPTION
		main()
