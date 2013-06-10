import sys
import json

def prepareSentiments(sent_file):

    afinnfile = open(sent_file)
    sent_scores = {}
    for i, sentLine in enumerate(afinnfile):
		word, score = sentLine.split("\t") 
		sent_scores[word.decode('utf-8')] = float(score)
    return sent_scores

def readTweets(sent_scores, tweet_file):
	tweet_file = open(tweet_file)
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0
		unscored_words = set()

		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			tweet_text = tweet_json['text'].encode('utf-8').lower()
			
			tweet_splited = tweet_text.split() 
			for word in tweet_splited:
				if word in sent_scores:
					tweet_sentiment += float(sent_scores[word])
				elif word not in unscored_words:
					unscored_words.add(word)
				print word
			print unscored_words
			print tweet_sentiment
			# tweet_sentiment = search_sentiments_in_text(sent_scores, tweet_text)
			# print "tweet_sentiment: %s, tweet_text: %s"%(str(tweet_sentiment), tweet_text)
	# print sent_scores

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_scores = prepareSentiments(sys.argv[1])
	tweet_file = sys.argv[2]
	readTweets(sent_scores, tweet_file)
    # tweet_file = open(sys.argv[2])
    # hw()
    # lines(tweet_file)

if __name__ == '__main__':
    main()
