import sys
import tweepy
from textblob import TextBlob
import pandas as pd

Sch = raw_input('Enter the topic you want to analyse: ')

cons_key = 'zu4P53o22o9GhW7agopxVIEmD'
cons_sec = 'Tlex6ORhVi6g2qJ7bWSCkY3Nmov3qPhZL3sHXXn3eItjmmJnUm'

acc_token = '720261503291555840-oM64Z1ENhtSAXMI5RCAxwZz7wTFmE9x'
acc_token_sec = 'U6Hc2qdtxLGStRFFUy7z7ktR1gNwEShNyoZsSEnkiGCSV'

auth = tweepy.OAuthHandler(cons_key,cons_sec)
auth.set_access_token(acc_token,acc_token_sec)

api = tweepy.API(auth)

Tweets = api.search(Sch)

Tweets_CSV = [["Tweets","Polarity"]]

for tweet in Tweets:
    twit = []
    Senti = "Positive".encode('utf-8').strip()
    twit.append(tweet.text.encode('utf-8').strip())
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity < 0:
        Senti = "Negative".encode('utf-8').strip()
    twit.append(Senti)
    Tweets_CSV.append(twit)

print Tweets_CSV

Sch += ' Tweets.csv'.encode('utf-8')
Tweets_DF = pd.DataFrame(Tweets_CSV)
Tweets_DF.to_csv(Sch,index = False,header = False,sep = ',')
