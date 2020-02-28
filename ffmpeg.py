# -*- coding: utf-8 -*-
# Author: Pat Rick Ntwari
# Assignment 4
# EC500
# Prof. Osama A. 
import io
import os
import subprocess

import time
import requests

import datetime
import textwrap
from io import BytesIO

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def makevideo(item):
  #command = "ffmpeg -i {video} -ac 1  -f flac -vn {output}".format(video=video, output=output)

  dest = '%s.mp4'%item
  cmd1 = 'ffmpeg -r 0.5 -f image2 -s 1920x1080 -i '
  cmd2 = '%s'%item
  cmd3 = '%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p '
  dest = '%s.mp4'%item
  command = cmd1+cmd2+cmd3+dest
  
  #print(command)

  # path=os.getcwd()
  # path=path+"/results/"
  # with cd(path):
  #   subprocess.call(command,shell=True)

  subprocess.call(command,shell=True)


def main():
  makevideo('ats')
  


if __name__ == '__main__':
  main()
 