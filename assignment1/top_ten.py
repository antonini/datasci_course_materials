import sys
import json
from operator import itemgetter, attrgetter


def prepareSentiments(sent_file):

    afinnfile = open(sent_file)
    sent_scores = {}
    for i, sentLine in enumerate(afinnfile):
		word, score = sentLine.split("\t") 
		sent_scores[word.decode('utf-8')] = float(score)
    return sent_scores

def readTweets(tweet_file):

	sum_terms = 0
	term_count = {}
	tweet_file = open(tweet_file)
	for tweet_line in tweet_file:
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			entities = tweet_json['entities']
			hashtags = entities['hashtags']
			for hashtag in hashtags:
				if ('text' in hashtag):
					hashText = hashtag['text'].encode('utf-8').replace('\n','')
					if hashText in term_count:
						term_count[hashText] += 1
					else:
						term_count[hashText] = 1

	term_count = sorted(term_count.iteritems(), key=itemgetter(1), reverse=True)
	top_x_items = []
	i = 0
	for hashtag_item in term_count:
		if (i < 10):
			top_x_items.append(hashtag_item)
			i += 1
		else:
			break
	
	for hashtag_data in top_x_items:
		print "%s %s"%(hashtag_data[0].encode('utf-8'), str(float(hashtag_data[1])))

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweet_file = sys.argv[1]
	readTweets(tweet_file)

if __name__ == '__main__':
    main()
