import tweepy, time
from tweepy import TweepError

class SameTweetException(BaseException):
	def __init__(self, message):
		self.message = message

class Tweet():
	def _init_(self):
		return null

	def postTweet(self, message, api):
		try:
			posted = api.update_status(status=message)	#I AM GONNA POST IT
		except tweepy.TweepError as err:				#SHIT I FAILED
			er_code = err.args[0][0]['code']
			print (er_code)
			if er_code == 187:							#So it was a duplicate tweet
				print("Cant tweet same thing twice")
				print("Raising an error")
				raise SameTweetException("Same Tweet")	#Let's throw an exception to be caught by someone else
				return()

			elif er_code == 186:						#Why the hell we can't post longer tweets
				print("Tweet to long")
				print("Slicing tweet")
				lenOfMessage = len(message)
				postTweet(message[0:135]+"+++", api)	#So let's post its first 135 char first
				postTweet(message[135:], api)			#And try to post remaining
				return()								#Done? Done.

			else:
				print ("Unexpected exception = \"{0}\"".format(err.args[0][0]['message'])) #What the heck? That was unexpected.
				postTweet(message, api) 				#I don't know what to do. So let's try to post it again.
		except Exception as er:
			postTweet(message, api)						#There was something wrong with internet i guess, so let's try again.

	def get_api(self, loc):  							#insert location of keys for auth. use return api value for posting
		try:
			foo = open(loc, "r")
			keys = foo.read().splitlines()
			foo.close()
			'''
			keys.txt's structure is like;

			consumer_token,KEY
			consumer_secret,KEY
			access_token,KEY
			access_secret,KEY
			'''
			cfg = {}								#It is config dictionary
			for line in keys:
				key_name = line.split(",")[0]
				key = line.split(",")[1]
				cfg[key_name] = key
			auth = tweepy.OAuthHandler(cfg['consumer_token'], cfg['consumer_secret'])
			auth.set_access_token(cfg['access_token'], cfg['access_secret'])	#authenticating
			return (tweepy.API(auth))
		except Exception:							#What? You can't even authenticate? Try again, you must do it
			return (get_api(loc))

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
			time.sleep(60)
		except SameTweetException:
			print("CAUGHT")
			tweet1.postTweet(lines1.getLine(), api)

if __name__ == "__main__":
	main()
