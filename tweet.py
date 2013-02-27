# tweet class for analyzing
# author : @ismailsunni
# contact : imajimatika@gmail.com
# created : 24/02/2012

class Tweet:
    def __init__(self, long_text=None):
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