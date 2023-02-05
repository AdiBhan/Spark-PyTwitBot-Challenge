import time

import settings
import tweepy


class TweepyBot:
    
    def __init__(self):
      # Initialize the bot  
      
        ## Create API object
        self.auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
        self.api = tweepy.API(self.auth)
        
    def tweet(self):
        ## Tweet a message
        return self.api.update_status("My first automated Tweet! #SparkFun #Python #Tweepy");
    
# Run the bot    
if __name__ == "__main__":
    bot = TweepyBot()
    bot.tweet()