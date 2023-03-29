# Bugged Version
import os

sys.path.append(os.getcwd() + '\settings')
import config
import tweepy


class TweepyBot:
    
    def __init__(self):
      # Initialize the bot  
      
        ## Create API object
        self.auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
        self.api = tweepy.API(self.auth)
        
    def tweet(self):
        ## Tweet a message
        print( self.api.update_tatus("My first automated Tweet! #SparkFun #Python #Tweepy"));
    
# Run the bot    
if name == "__main__":
    bot = TweepyBot()
    bot.tweet("Hi")