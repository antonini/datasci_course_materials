import sys
import json
import csv
import re
from collections import Counter
import operator

def get_user_mentions(text):
    twitter_username_re = re.compile(r'@([A-Za-z0-9_]+)')
    return re.findall(twitter_username_re, text)

def get_urls(text):
    url_re = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    res = re.findall(url_re, text)
    return res

def remove_nonalpha(text):
	pattern = re.compile("[^\w']")
	text = pattern.sub(' ', text)

	return text

def remove_urls(text):
	urls = get_urls(text)

	for url in urls:
		text = text.replace(url,"")
	
	return text	

def remove_mentions(text):
	mentions = get_user_mentions(text)
	for mention in mentions:
		mention = "@"+mention
		text = text.replace(mention,"")
	
	return text	

def clean_text(text):
	text = remove_mentions(text)
	text = remove_urls(text)
	text = remove_nonalpha(text)

	return text

def tokenize(text):
	text = clean_text(text)
	return text

def load_terms_scores(sent_file):
	afinnfile = open(sent_file)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.

	return scores

def compute_tweet_sentiment(tweet_text,terms_scores):
	tweet_text = tokenize(tweet_text)
	tweet_terms = tweet_text.split(" ")

	tweet_sentiment = 0
	for term in tweet_terms:
		term = term.lower()

		if (terms_scores.has_key(term)):
			term_sentiment_score = terms_scores.get(term)
			tweet_sentiment = tweet_sentiment + term_sentiment_score

	return tweet_sentiment

def decode_state_by_country(country_code,tweet):
	# country_code,full_name,name,place_type
	if(tweet.has_key("place")):
		place = tweet["place"]
		if not(place == None):
			if(place["country_code"] == country_code):
				state_code = place["full_name"].split(",")[1]
				state = state_code.encode("utf-8").strip()			
				return state


def load_tweets(tweets_file):
	tweets_file = open(tweets_file)
	tweets = list() # initialize an empty list
	
	for line in tweets_file:
		tweet = json.loads(line)
		tweets.append(tweet)

	return tweets	

def decode_sentiment_label(sentiment):
	sentiment_label = "neutral"
	if(sentiment > 0):
		sentiment_label = "positive"
	else: 
		if (sentiment < 0):	
			sentiment_label = "negative"

	return sentiment_label 				

def hw(sent_file,tweet_file):

    terms_scores = load_terms_scores(sent_file)
    tweets = load_tweets(tweet_file)

    sentiment_by_country = {}
    for tweet in tweets:
		sentiment = 0
		#makes sure if it's a tweet
		if(tweet.has_key("text")):
			#verify if tweet is in english
			# if(tweet["user"]["lang"] == "en"):
			# 	tweets.append(tweet)

			sentiment = compute_tweet_sentiment(tweet["text"],terms_scores)
			state_code = decode_state_by_country("US",tweet)
			
			if not(state_code == None):

				if not(sentiment_by_country.has_key(state_code)):
					sentiment_by_country[state_code] = 0
					
				sentiment_by_country[state_code] = sentiment_by_country[state_code] + sentiment				
				# print sentiment

    # sentiment_by_country = filter(None, sentiment_by_country)
 #    for country in sentiment_by_country.keys():
 #    	print country, sentiment_by_country[country]

	# print "--"
    happiest_states = list(sorted(sentiment_by_country, key=sentiment_by_country.__getitem__, reverse=True))
 #    for happy_state in happiest_states:
 #    	print happy_state

    if len(happiest_states) > 0:
    	# "Happiest state"
    	print happiest_states[0]

    # print sorted(sentiment_by_country.values())
    	# print state[0].encode("utf-8"),float(state[1])	

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
