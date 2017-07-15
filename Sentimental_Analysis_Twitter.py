import sys
import tweepy
from textblob import TextBlob

Sch = raw_input('Enter the topic you want to analyse: ')

cons_key = 'zu4P53o22o9GhW7agopxVIEmD'
cons_sec = 'Tlex6ORhVi6g2qJ7bWSCkY3Nmov3qPhZL3sHXXn3eItjmmJnUm'

acc_token = '720261503291555840-oM64Z1ENhtSAXMI5RCAxwZz7wTFmE9x'
acc_token_sec = 'U6Hc2qdtxLGStRFFUy7z7ktR1gNwEShNyoZsSEnkiGCSV'

auth = tweepy.OAuthHandler(cons_key,cons_sec)
auth.set_access_token(acc_token,acc_token_sec)

api = tweepy.API(auth)

Tweets = api.search(Sch)

for tweet in Tweets:
    print
    print tweet.text
    analysis = TextBlob(tweet.text)
    print analysis.sentiment
    print 
