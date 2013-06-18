import sys
import json
import csv
import re

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
	# text = remove_mentions(text)
	# text = remove_urls(text)
	# text = remove_nonalpha(text)

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
		
	for term in tweet_terms:
		if not(terms_scores.has_key(term)):
			compute_term_sentiment_score(term,tweet_sentiment)
		
	return tweet_sentiment

def compute_term_sentiment_score(term,tweet_sentiment):
	term_sentiment = tweet_sentiment
	
	if (new_terms_scores.has_key(term)):
		term_sentiment_score = new_terms_scores.get(term)
		term_sentiment = term_sentiment + term_sentiment_score
	
	new_terms_scores[term] = term_sentiment 


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

	for tweet in tweets:
		sentiment = 0
		#makes sure if it's a tweet
		if(tweet.has_key("text")):
			sentiment = compute_tweet_sentiment(tweet["text"],terms_scores)


	for new_term in new_terms_scores:
		if not(new_term == "" or new_term == " "):
			print new_term.encode("utf-8"),float(new_terms_scores[new_term])

new_terms_scores = {}
def main():
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
	hw(sent_file,tweet_file)

if __name__ == '__main__':
	main()
