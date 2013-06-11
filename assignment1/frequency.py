import sys
import json

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
			tweet_text = tweet_json['text'].encode('utf-8').replace('\n','').lower()
			
			tweet_splited = tweet_text.split() 
			for word in tweet_splited:
				sum_terms += 1
				if word in term_count:
					term_count[word] += 1
				else:
					term_count[word] = 1
	for term, count in term_count.items():
		calc = float(count) / float(sum_terms)
		print "%s %s"%(term, str(calc))

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweet_file = sys.argv[1]
	readTweets(tweet_file)
    # tweet_file = open(sys.argv[2])
    # hw()
    # lines(tweet_file)

if __name__ == '__main__':
    main()
