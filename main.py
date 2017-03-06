from Lines import Lines
from Tweet import Tweet
from SameTweetException import SameTweetException
import time

def main():
	keysLoc = "keys.txt"
	linesLoc = "adim garavel.txt"
	tweet1 = Tweet()
	lines1 = Lines(linesLoc)
	api = tweet1.get_api(keysLoc)
	while True:
		try:
			message = lines1.getLine()
			print(message)
			tweet1.postTweet(message, api)
			time.sleep(15)
		except SameTweetException:
			tweet1.postTweet(lines1.getLine(), api)

if __name__ == "__main__":
	try:
		main()
	except Exception:  #HA HA YOU CAN'T ESCAPE EXCEPTION
		main()
