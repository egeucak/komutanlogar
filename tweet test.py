import tweepy
from tweepy import TweepError

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_token'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_secret'])
	return (tweepy.API(auth))


def main():
	keys = open("keys.txt", "r").read().splitlines()
	cfg = {}
	for line in keys:
		key_name = line.split(",")[0]
		key = line.split(",")[1]
		cfg[key_name] = key

	api = get_api(cfg)
	while True:
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
			break
		except Exception as er:
			print ("farkli hata {0}".format(er))
		#break

if __name__ == "__main__":
	main()
