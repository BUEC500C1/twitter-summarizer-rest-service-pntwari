# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 3
# EC500
# Prof. Osama A. 

import tweepy #https://github.com/tweepy/tweepy
import json
from twitter_keys import key_def
import os
import string
import re
import sys
#import panda as pd
import string
import threading
import textwrap

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def remove_at(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
        
    return input_txt 
  
def remove_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text
  
def gettweets(company):
  #Twitter API credentials
  key = key_def()
  consumer_key = key[0]
  consumer_secret = key[1]
  access_key = key[2]
  access_secret = key[3]

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  tweet_text = []

  #print("about to pull tweets")

  if consumer_key == "NA":
    with open('example.txt') as f:
      for line in f:
        tweet_text.append(line)

  else: 

    #for tweet in tweepy.Cursor(api.search,q=company,count=1,lang="en",since ="2020-02-10", tweet_mode = 'extended').items():
    for tweet in tweepy.Cursor(api.search,q=company,count=1,lang="en",tweet_mode = 'extended').items(3):
      #if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
      #text=remove_at(tweet.full_text.encode("utf-8"),"@[\w]*")
      text=str(tweet.full_text.encode("utf-8"))
      text=remove_emoji(text)
      text=remove_at(text,"@[\w]*")
      text=remove_at(text,"RT[\w]*")
      #text=remove_at(text,"#[\w]*")
      text=remove_at(text,"$[\w]*")
      text=remove_at(text,"x[\w]*")
      text=remove_at(text,"b'*")
      text = textwrap.fill(text, width=70)
      tweet_text.append(remove_links(text))
    #with open('tesla_tweets.txt', 'w') as f:
    #  f.write('\n'.join(tweet_text))


  return tweet_text


  # with open('%s.txt' %company, 'w') as f:
  #   f.write('\n'.join(tweet_text))
  
  

  
if __name__ == '__main__':
    #pass in the username of the account you want to download
    tweets = gettweets("Paris")
    for item in tweets:
      print(item)
    print(type(tweets))