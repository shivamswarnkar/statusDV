 import tweepy


class Timeline:
    def __init__(self, app=None):
        """A wrapper object which works with flask app and
        loads user tweets by making api calls to twitter through tweepy.
        give a flask app at either object creation or call init_app method later.
        
        app.config must have valid values for following keys
            'TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET',
            'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET'

        Args:
            app: flask app with required twitter key configuration
        """
        self.api = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        initiates twitter api authorization, and creates tweepy.API 
        object for future use. app.config must have valid values for 
        following keys
            'TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET',
            'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET'

            Args:
                app: A flask app with required twitter key configuration
            Returns:
                None
        """
        auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'], 
                                   app.config['TWITTER_CONSUMER_SECRET'])
        auth.set_access_token(app.config['TWITTER_ACCESS_TOKEN'], 
                              app.config['TWITTER_ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def get_tweets(self, handle, exclude_replies=True, include_rts=False, min_count=50):
        """
        initiates twitter api authorization, and creates tweepy.API 
        object for future use.

            Args:
                handle (str): handle name of the user whose tweets will be retrieved
                exclude_replies (bool, default=True): does not retrieve replies
                include_rts (bool, default=False): include re-tweets
                min_count (int, default=50): min numbers of tweets to be retrieved 
            Raises:
                Exception if class object does not have access to a flask app 
                with required twitter key configurations
            Returns:
                list of user tweets. Empty list if api call fails or user 
                didn't have any tweets
        """
        # check if proper app configuration was provided
        if self.api is None:
            return Exception('App not initiated. Cannot load api.')
        
        lst = []  # variable to store retrieved tweets
        timeline = ['', '']  # variable to store value returned from api calls
        max_id = None  # latest tweet id from last api call
        
        # while api call returned non-empty values and tweet counts is less than min_count
        # retrieve tweets
        while len(timeline) > 1 and len(lst) < min_count:
            timeline = self.api.user_timeline(handle,
                                              tweet_mode='extended',
                                              exclude_replies=exclude_replies,
                                              include_rts=include_rts,
                                              max_id=max_id,
                                              count=min_count)
            max_id = timeline[-1]._json['id_str']
            lst.extend([status._json['full_text'] for status in timeline])
            
        return lst   # return lst of tweets
