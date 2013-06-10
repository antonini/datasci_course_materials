import sys
import json

def hw():
    print 'Hello, world!'

def prepareSentiments(sent_file):
	sent_file = open(sent_file)
	sent_scores = []
	for i, sentLine in enumerate(sent_file):
		term, score = sentLine.split("\t")
		sent_scores.append((term, int(score)))
	return sent_scores

def readTweets(sent_scores, tweet_file):
	tweet_file = open(tweet_file)
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0

		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			tweet_text = tweet_json['text'].encode('utf-8').lower()

			print tweet_text
			
			tweet_sentiment = search_sentiments_in_text(sent_scores, tweet_text)
			# print "tweet_sentiment: %s, tweet_text: %s"%(str(tweet_sentiment), tweet_text)
			

def search_sentiments_in_text(sent_scores, tweet_text):
	total_sentiment = 0.0
	for i in range(len(sent_scores)):
		total_sentiment += search_sentiment_in_text(sent_scores[i], tweet_text)
	return total_sentiment

def search_sentiment_in_text(sentiment, tweet_text):
	total_sentiment = 0.0
	term = sentiment[0]
	score = sentiment[1]
	term_count = tweet_text.count(term)
	total_sentiment = term_count * score
	if term_count > 0:
	    print "%s:%s" %(term, total_sentiment)
	return total_sentiment


def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_scores = prepareSentiments(sys.argv[1])
	tweet_file = sys.argv[2]

	# print sent_scores
	readTweets(sent_scores, tweet_file)

if __name__ == '__main__':
    main()
