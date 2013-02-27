# script to analysis your tweets
# author : @ismailsunni
# contact : imajimatika@gmail.com
# created : 24/02/2012

from tweet import Tweet
from utilities import sort_dict
import csv
import os

class TweetAnalysis:
    def __init__(self, data_path, my_username=None):
        self.data_path = data_path
        self.tweet_data = []
        self.username = my_username
        self.extract_data()

    def extract_data(self):
        """Extract raw data to list of tweet object.
        """
        try:
            f = open(self.data_path, 'rb')
            csv_reader = csv.reader(f)
            csv_reader.next()
            for my_element in csv_reader:
                my_tweet = Tweet()
                my_tweet.parse_list(my_element)
                self.tweet_data.append(my_tweet)
            f.close()
        except IOError as e:
            print 'Error : ', e
            raise e

    def analyze_reply_to(self, num_user=10):
        """Return the 10 highest user you reply to.
        """
        dict_user_id = {}
        for my_tweet in self.tweet_data:
            if my_tweet.in_reply_to_user_id == '':
                continue
            if my_tweet.in_reply_to_user_id not in dict_user_id:
                dict_user_id[str(my_tweet.in_reply_to_user_id)] = 1
            else:
                dict_user_id[str(my_tweet.in_reply_to_user_id)] += 1
        retval = sort_dict(dict_user_id, num_elements=num_user)
        return retval

    def analyze_retweeted_status_user_id(self, num_user=10):
        """Return the 10 highest user you retweeted_status_user_id.
        """
        dict_user_id = {}
        for my_tweet in self.tweet_data:
            if my_tweet.retweeted_status_user_id == '':
                continue
            if my_tweet.retweeted_status_user_id not in dict_user_id:
                dict_user_id[str(my_tweet.retweeted_status_user_id)] = 1
            else:
                dict_user_id[str(my_tweet.retweeted_status_user_id)] += 1
        retval = sort_dict(dict_user_id, num_elements=num_user)
        return retval

    def analyze_source(self, num_user=10):
        """Return the 10 highest user your source.
        """
        dict_user_id = {}
        for my_tweet in self.tweet_data:
            if my_tweet.source == '':
                continue
            if my_tweet.source not in dict_user_id:
                dict_user_id[str(my_tweet.source)] = 1
            else:
                dict_user_id[str(my_tweet.source)] += 1
        retval = sort_dict(dict_user_id, num_elements=num_user)
        return retval
        
def main():
    my_path = r'D:\Kode\TweetAnalytics\tweets.csv'
    my_TweetAnalysis = TweetAnalysis(my_path)
    if my_TweetAnalysis.tweet_data is None:
        print 'Tweet data is None'
    else:
        my_TweetAnalysis.tweet_data[0].print_tweet()
        a = my_TweetAnalysis.analyze_reply_to(20)
        c = my_TweetAnalysis.analyze_retweeted_status_user_id(20)
        e = my_TweetAnalysis.analyze_source(20)
        print '------------------------------------'
        print 'replied status user id'
        print '------------------------------------'
        for b in a:
            print b[0], b[1]
        print '------------------------------------'
        print 'retweeted status user id'
        print '------------------------------------'
        for d in c:
            print d[0], d[1]
        print '------------------------------------'
        print 'source'
        print '------------------------------------'
        for f in e:
            print f[0], f[1]

if __name__ == '__main__':
    main()