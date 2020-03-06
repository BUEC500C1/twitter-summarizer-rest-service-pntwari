# video-pntwari
video-pntwari created by GitHub Classroom

## Author:
This project is created under the direction of Osama Alshaykh of Boston University as Homework 5 for EC500. 
Spring 2020.

## Introduction

This is a continuation of HW4. It builds on HW5 in that it adds the entire system into the REST framework whose core is provided by Flask. 
Just like the original project, this code calls a few subcoded with the intent of creating a video with a summary of the most recent tweets about a certain topic. 
Much like last time, the example shown in here is not quite real, as an example file was given so as to preserve the Twitter API keys. 

One file from the original submission is edited and another is added. The modified is ffmpeg.py and the new one is basic.py

## How to Use
Usage is simple. 
There are several core codes: 
- main.py
- twitter.py
- makeimage.py
- ffmpeg.py
- basic.py

Within main.py, there is a function processtwitter(). 
This is the central and brain of this procedure. 

However, calling is done through the end by calling the return url of what topic you would like to see a video for. 
For example: 127.0.0.1/google returns, hypothecally, the most recent tweets regarding Google. 

All the previous functions are still done. A front end web end is added. 
