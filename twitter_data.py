import tweepy
import json
import re
import csv

# Function to extract tweets 
def get_tweets(query, cnt = 20):        
        # Get API Secrets from json file        
        secrets = json.loads(open('files/auth.json').read())
        api_key = secrets['api_key']
        api_secret = secrets['api_secret_key']
        access_token = secrets['access_token']
        access_token_secret = secrets['access_token_secret']

        try:
            # Authorization to consumer key and consumer secret 
            auth = tweepy.OAuthHandler(api_key, api_secret) 

            # Access to user's access key and access secret 
            auth.set_access_token(access_token, access_token_secret) 

            # Calling api 
            api = tweepy.API(auth) 
    
        except:
            print('Error: Authentication Failed.')
        
         # Empty Array 
        tweets=[]
        
        fetched_tweets = list(tweepy.Cursor(api.search, q=query, lang='en', result_type='recent').items(cnt))
        #api.search(q = query, lang = 'en', count = cnt)             
        for tweet in fetched_tweets:
            tweet_text = re.sub(r"http\S+", "", tweet.text)            
            regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags = re.UNICODE)
            tweet_text = regrex_pattern.sub(r'', tweet_text)                      
            tweets.append(tweet_text)                                        
        
        with open('files/project_twitter_data.csv', 'w', newline='', encoding = 'utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['tweet_text'])
            for tweet in tweets:
                writer.writerow([tweet])                        
