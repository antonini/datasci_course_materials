import sys
from collections import Counter
import re
import json

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
	text = text.replace("  "," ")

	return text

def tokenize(text):
	text = clean_text(text)
	return text

def load_tweets(tweets_file):
	tweets_file = open(tweets_file)
	tweets = list() # initialize an empty list
	
	for line in tweets_file:
		tweet = json.loads(line)
		tweets.append(tweet)

	return tweets

def compute_frequency(term_freq,freq_all_terms):
	# [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
	result = float( ( term_freq ) ) / ( freq_all_terms )

	return round(result, 4)

def hw(tweet_file):
	tweets = load_tweets(tweet_file)

	all_terms = list()
	for tweet in tweets:
		if(tweet.has_key("text")):
			tweet_text = tweet["text"]

			tweet_text = tokenize(tweet_text)
			tweet_terms = tweet_text.split(" ")
			all_terms = all_terms + tweet_terms

	# print len(all_terms)
	all_terms = filter(None, all_terms)
	
	c = Counter(all_terms)
	terms_dict = {}
	for term in c.most_common():
		term_freq = compute_frequency(term[1],len(all_terms))
		terms_dict[term[0]] =  term_freq		
		
	cf = Counter(terms_dict)
	for cfterm in cf.most_common():
		print cfterm[0].encode("utf-8"),float(cfterm[1])

def main():
    tweet_file = sys.argv[1]
    hw(tweet_file)
    
if __name__ == '__main__':
    main()

