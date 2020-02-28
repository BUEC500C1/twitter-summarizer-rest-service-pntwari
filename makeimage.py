# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 3
# EC500
# Prof. Osama A. 
import io
import os
import subprocess

import time
import requests
import queue

import datetime
import textwrap
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

# fonts_dir = os.path.join(os.environ['WINDIR'], 'Fonts')
# font_name = 'consolab.ttf'
# font = ImageFont.truetype(os.path.join(fonts_dir, font_name), 15)

def makevideo():
    command = "ffmpeg -i {video} -ac 1  -f flac -vn {output}".format(video=video, output=output)
    command = "ffmpeg -r 60 -f image2 -s 1920x1080 -i %d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p test.mp4"
    subprocess.call(command,shell=True)


#def makeimages(item,tweet,count):
def makeimages(item,tweets):
  background = Image.new('RGBA', (1024, 768), (255, 255, 255, 255))
  draw = ImageDraw.Draw(background)
  #tweet = textwrap.wrap(tweet, width=80)
  #font = ImageFont.load("arial.pil")
  x, y = 10, 50

  #item=item[1:]     #take off hashtag

  if os.path.isdir("results") == False:
    path=os.getcwd()
    new="results"
    try:
      os.mkdir(new)
    except OSError:
        print ("Creation of the directory %s failed" % new)
    else:
        print ("Successfully created the directory %s " % new)

  # draw.text((x, y),str(tweet),(100,100,200))#,font=font)
  # y += 20
  # background.save('./images/%s'%item+str(count)+'.png')
  count = 0
  for tweet in tweets:
    tweet = textwrap.wrap(tweet, width=80)
    draw.text((x, y),str(tweet),(100,100,200))#,font=font)
    y += 20
    background.save('./results/%s'%item+str(count)+'.png')
    count+=1

def main():

  tweets = []
  with open('#Coffee.txt') as f:
    for line in f:
      tweets.append(line)
      #print("whew ", line)
  makeimages('#Coffee',tweets)


if __name__ == '__main__':
  main()
 
