import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
	def __init__(self):
		# keys and tokens from Twitter API
		c_key = ""
		c_secret = ""
		a_token = ""
		a_token_secret = ""
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
	def get_tweets(self, query, count = 10):
		tweets = []

		try:
			fetched_tweets = self.api.search(q = query, count = count)
			for t in fetched_tweets:
				parsed_tweet = {}
				parsed_tweet['text'] = t.text
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(t.text)
				if t.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
					else:
						tweets.append(parsed_tweet)
			return tweets
		except tweepy.TweepError as e:
			print("Error: " + str(e))
def main():
	api = TwitterClient()
	tweets = api.get_tweets(query = 'Supreme Box', count = 200)
	posTweets = [tweet for t in tweets if tweet['sentiment'] == 'positive']
	print("Positive tweets percentage: {} % ".format(100*len(posTweets)/len(tweets)))
	negTweets = [tweet for t in tweets if tweet['sentiment'] == 'negative']
	print("Negative tweets percentage: {} % ".format(100*len(negTweets)/len(tweets)))
	neuTweets = [tweet for t in tweets if tweet['sentiment'] == 'neutral']
	print("Neutral tweets percentage: {} % ".format(100*len(neuTweets)/len(tweets)))
	#printing all of the tweets
	print("\n\nPositive Tweets:")
	for tweet in posTweets[:5]:
		print(tweet['text'])
	print("\n\nNegative Tweets")
	for tweet in negTweets[:5]:
		print(tweet['text'])
	print("\n\nNeutral Tweets")
	for tweet in neuTweets[:5]:
		print(tweet['text'])
if __name__ == "__main__":
	main()
