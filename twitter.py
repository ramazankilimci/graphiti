from os import truncate
import tweepy
import csv
import sys

consumer_key = "l1hj0T39dSfWc9KsXUnpS1Zur"
consumer_secret = "I9SU6sRbk8TcHn7aQHo0YiP446vyTYCN0hCEOaj584yc78DUYK"
access_token = "2241277500-cqXWlHLmmr8RHWxGZe5pnoN3LDQzWi6jnS39k0N"
access_token_secret = "3XEqQyEBFWiO7oTBKlQnLOvXc3RMH0oGwEnx6hITHuS5n"

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# Open/create a file to append data to
# csvFile = open('result.csv','a', encoding='utf-8')

import pandas as pd
keyword_to_search = 'Gezi'
# public_tweets = api.home_timeline()
public_tweets = api.search_tweets(q = keyword_to_search, lang='en', count=100, tweet_mode='extended')
# print(public_tweets)
tweets = []

for tweet in public_tweets:
    print(tweet._json['created_at'], tweet._json['full_text'])
    tweets.append([tweet._json['created_at'], tweet._json['full_text']])

df = pd.DataFrame(tweets, columns=['date', 'tweet'])
df.to_csv("data.csv", mode='a', index=False)

