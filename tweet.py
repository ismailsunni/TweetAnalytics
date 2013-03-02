# tweet class for analyzing
# author : @ismailsunni
# contact : imajimatika@gmail.com
# created : 24/02/2012

from ttp import Parser

class Tweet:
    def __init__(self, long_text=None):
        """Init function for tweet.
        """
        self.parser = Parser()
        if long_text is not None:
             self.parse_string()
        else:
            self.tweet_id = ''
            self.in_reply_to_status_id = ''
            self.in_reply_to_user_id = ''
            self.retweeted_status_id = ''
            self.retweeted_status_user_id = ''
            self.timestamp = ''
            self.source = ''
            self.text = ''
            self.expanded_urls = ''

    def parse_list(self, list_element):
        """Parse tweet from list.
        """
        self.tweet_id = list_element[0]
        self.in_reply_to_status_id = list_element[1]
        self.in_reply_to_user_id = list_element[2]
        self.retweeted_status_id = list_element[3]
        self.retweeted_status_user_id = list_element[4]
        self.timestamp = list_element[5]
        self.source = list_element[6]
        self.text = list_element[7]
        if len(list_element) == 9:
            self.expanded_urls = list_element[8]

    def get_mentions(self):
        """Return list of user mentioned in the tweet.
        Return empty list if no user mentioned.
        """
        my_users = self.parser.parse(self.text).users
        return my_users

    def get_hashtags(self):
        """Return list of hashtag in the tweet.
        Return empty list if no hashtag used.
        """
        my_hashtags = self.parser.parse(self.text).tags
        return my_hashtags

    def print_tweet(self):
        """Print tweet in beautiful format
        """
        print 'tweet_id : ', self.tweet_id
        print 'in_reply_to_status_id : ', self.in_reply_to_status_id
        print 'in_reply_to_user_id : ', self.in_reply_to_user_id
        print 'retweeted_status_id : ', self.retweeted_status_id
        print 'retweeted_status_user_id : ', self.retweeted_status_user_id
        print 'timestamp : ', self.timestamp
        print 'source : ', self.source
        print 'text : ', self.text
        print 'expanded_urls : ', self.expanded_urls


def main():
    """For testing some function in this file
    """
    my_tweet = Tweet()
    my_tweet.text = '@dinolestari @Ardisaz @widhaprasa Kalau gak hari sabtu ya hari minggu din #apem'
    print my_tweet.get_mentions()
    print my_tweet.get_hashtags()

if __name__ == '__main__':
    main()