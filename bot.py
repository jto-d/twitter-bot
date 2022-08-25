import tweepy
import time

# api keys redacted

consumer_key = ''
consumer_secret = ''

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

word1 = 'lee chan'
word2 = 'dino rt bot'
tweetnumber = 10

# store last_seen tweets in a file for testing
"""
FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write_close()
    return
"""

def search_bot(phrase):
    tweets = tweepy.Cursor(api.search, phrase).items(tweetnumber)
    for tweet in tweets:
        tweetText = tweet.text.lower()
        if phrase in tweetText:
            try: 
                tweet.retweet()
                print("Retweet done!")
                time.sleep(2)
            except tweepy.TweepError as e:
                print(e.reason)
                time.sleep(2)

def search_bot2(phrase):
    tweets = tweepy.Cursor(api.search, phrase).items(tweetnumber)
    for tweet in tweets:
        try:  
            tweet.retweet()
            print("Retweet done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

while(True):
    search_bot(word1)
    search_bot2('dino rt bot')
    time.sleep(300)

