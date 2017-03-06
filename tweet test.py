import tweepy
from tweepy import TweepError

class Tweet:
	def _init_(self):
		return null

	def postTweet(self, message, api):
		try:
			posted = api.update_status(status=message)
		except tweepy.TweepError as err:
			er_code = err.args[0][0]['code']
			print (er_code)
			if er_code == 187:		#duplicate tweet error
				print("Cant tweet same thing twice")
				print("Generating a new message")
				message = Lines(loc).getLine()
				postTweet(message, api)
				return()


			elif er_code == 186:	#long tweet error
				print("Tweet to long")print("Slicing tweet")
				lenOfMessage = len(message)
				postTweet(message[0:135]+"+++", api)
				postTweet(message[135:], api)
				return()
			else:
				print ("Unexpected exception = \"{0}\"".format(err.args[0][0]['message']))
				postTweet(message, api)
		except Exception as er:
			postTweet(message, api)

	def get_api(self, loc):  #insert location of keys for auth. use return api value for posting
		try:
			keys = open(loc, "r").read().splitlines()
			cfg = {}
			for line in keys:
				key_name = line.split(",")[0]
				key = line.split(",")[1]
				cfg[key_name] = key
			auth = tweepy.OAuthHandler(cfg['consumer_token'], cfg['consumer_secret'])
			auth.set_access_token(cfg['access_token'], cfg['access_secret'])
			return (tweepy.API(auth))
		except Exception: #if an exception is raised, it tries to get api again.
			return (get_api(loc))


class Lines:
	lineLoc = ""
	def __init__ (self, loc):
		Lines.lineLoc = loc
		try:
			import random
		except ImportError:
			self.random = None
		else:
			self.random = random

	def getLine(self):
		file = open(Lines.lineLoc, "r", encoding='cp1254')
		garavel = file.read().splitlines()
		file.close()
		return (self.random.choice(garavel).strip())


def main():
	keysLoc = "keys.txt"
	linesLoc = "adim garavel.txt"
	tweet1 = Tweet()
	lines1 = Lines(linesLoc)
	print (lines1.getLine())
	api = tweet1.get_api(keysLoc)
	message = "Arif gelirken imam hatipleri kapatır mısın?"
	while True:
		tweet1.postTweet(message, api)



	"""keys = open("keys.txt", "r").read().splitlines()
	cfg = {}
	for line in keys:
		key_name = line.split(",")[0]
		key = line.split(",")[1]
		cfg[key_name] = key

	api = get_api(cfg)"""
	"""while True:
		try:
			status = api.update_status(status="ali babanın çifliğindeki orospu çocuğu öküzlerden bir farkın olsun be ekmek kafalı elmır salağı senin ananın amına fırıncı küreği sokayım imam hatipler kapatılsın")
			break
		except tweepy.TweepError as err:
			er_code = err.args[0][0]['code']
			print (er_code)
			if er_code == 187:
				print("Cant tweet same thing twice")
			elif er_code == 186:
				print("Tweet to long")
			else:
				print ("Unexpected exception = \"{0}\"".format(err.args[0][0]['message']))
			break
		except Exception as er:
			print("******")
			print (er)
			print("******")
		#break"""

if __name__ == "__main__":
	main()
