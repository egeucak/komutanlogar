from tweepy import TweepError
import tweepy

class Tweet():
	def _init_(self):
		return null

	def postTweet(self, message, api):
		try:
			posted = api.update_status(status=message)	#I AM GONNA POST IT
		except tweepy.TweepError as err:				#SHIT I FAILED
			if 'code' in err.args[0][0]:
				er_code = err.args[0][0]['code']
			else:
				er_code = 404
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
				print(lenOfMessage)
				self.postTweet(message[0:135]+"+++", api)	#So let's post its first 135 char first
				self.postTweet("+++"+message[135:], api)			#And try to post remaining
				return()								#Done? Done.

			else:
				print ("Unexpected exception = \"{0}\"".format(err)) #What the heck? That was unexpected.
				self.postTweet(message, api) 				#I don't know what to do. So let's try to post it again.
		except Exception as er:
			self.postTweet(message, api)						#There was something wrong with internet i guess, so let's try again.

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
