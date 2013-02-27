# script to analysis your tweets
# author : @ismailsunni
# contact : imajimatika@gmail.com
# created : 24/02/2012

from tweet import Tweet
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

def main():
    my_path = r'D:\Kode\TweetAnalysis\tweets.csv'
    my_TweetAnalysis = TweetAnalysis(my_path)
    if my_TweetAnalysis.tweet_data is None:
        print 'Tweet data is None'
    else:
        my_TweetAnalysis.tweet_data[0].print_tweet()

if __name__ == '__main__':
    main()