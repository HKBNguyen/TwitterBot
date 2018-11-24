import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	def __init__(self):
		# keys and tokens from Twitter API
		c_key = "D3SzTe0GP2ms4c2tp6yipxCrX"
		c_secret = "b7G00uthqd973hRIOtZvdZR6JpSALvDBns2QKZ8mHUnBQciJzt"
		a_token = "1066144772987842560-oQgR2lrHSOya1SvD7E0SP9a7yo6RgY"
		a_token_secret = "UBu1VY6iIdfNW2iMnLg1ewrLimnYtQcpcysD0gUrP7jcX"
		try:
			self.auth = OAuthHandler(c_key, c_secret)
			self.auth.set_access_token(a_token, a_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Authentication Failure")
	def clean(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())
	def get_sentiment(self, tweet):
		analysis = TextBlob(self.clean(tweet))
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity < 0:
			return 'negative'
		else:
			return 'neutral'