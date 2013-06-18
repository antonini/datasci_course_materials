import sys
import json
import csv
import re
from collections import Counter
from collections import defaultdict

def get_hashtags(tweet):
	result = list()

	if(tweet.has_key("entities")):
		if(tweet["entities"].has_key("hashtags")):
			hashtags = tweet["entities"]["hashtags"]
			for hashtag in hashtags:
				text = hashtag["text"]
				result.append(text)

	return result		

def load_tweets(tweets_file):
	tweets_file = open(tweets_file)
	tweets = list() # initialize an empty list
	
	for line in tweets_file:
		tweet = json.loads(line)
		tweets.append(tweet)

	return tweets	

def hw(tweet_file):

	tweets = load_tweets(tweet_file)
	
	all_hashtags = list()
	for tweet in tweets:
		if(tweet.has_key("text")):
			tweet_hashtags = get_hashtags(tweet)
			if(len(tweet_hashtags) > 0):
				all_hashtags = all_hashtags + tweet_hashtags

	c = Counter(all_hashtags)
	top10 = c.most_common(10)
	for hashtag in top10:
		print hashtag[0].encode("utf-8"),float(hashtag[1])
	

def main():
    tweet_file = sys.argv[1]
    hw(tweet_file)

if __name__ == '__main__':
    main()
