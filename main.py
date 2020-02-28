# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 3
# EC500
# Prof. Osama A. 

from twitter import gettweets
from makeimage import makeimages
from ffmpeg import makevideo
import os
import sys
import threading
import queue
import requests
import multiprocessing
import subprocess
import time

level = 0

def cb_func():
    "The callback function."
    print("Callback, in thread %s" %(threading.current_thread().name))

# Function that queuecontains all code for getting tweets then when the tweets are gotten
# create the images.
# then create the video
def th_func(q):
  global level
  while True:
    tweets = []
    item = q.get()
    # if(item == "Celtics"):
    #   time.sleep(10)
    # if(item == "Cats"):
    #   time.sleep(10)
    # if(item == "Boston"):
    #   time.sleep(10)

    if item is None: break
    try:
      print("getting some tweets for %s"%item)
      tweets = gettweets(item)
    except: 
      print("error in getting tweets")
      #return -1
    if len(tweets) > 0:
      try:
      # now create the images
        print("getting some images")
        makeimages(item,tweets)
      except:
        print("error in making images")
      # now create the video
      try:
        print("getting a video")
        makevideo(item)
      except:
        print("error making video")
    level = level - 1

    q.task_done()

#class myQueue():



def processtwitter(job):
  #myQueue
  global level 
  q = queue.Queue(maxsize=2)
  level = level+1
  print(level)
  while(level > 2):
    time.sleep(1)

  t = threading.Thread(name="Thread Processor:" + "0", target=th_func , args=(q,))
  t.start()
  print("running %s"%job)

  q.put(job)


  for i in range(2):
    q.put(None)
  # for t in threads:
  #   t.join(

if __name__ == '__main__':
  processtwitter("Stock")
  #processtwitter("Ash")
  #processtwitter("Tesla")

