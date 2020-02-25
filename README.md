# video-pntwari
video-pntwari created by GitHub Classroom

## Author:
This project is created bunder the direction of Osama Alshaykh of Boston University as Homework 4 for EC500. 
Spring 2020.

## Introduction

The files herein contribute to an a project whose design is to pull tweets about a certain topic and produce a video 
summarizing those tweets. 

The codes perform several functions:
- create a queue of (2) for video requests in case there are several entities calling the service
- create simultaneous threads (total of 2) that may run at the same time
- download the tweets (3 at a time) on any topic of choice. This number is easily adjustable
- create a cumulative images for these tweets i.e. create several images where the tweets add on, like a Microsoft Powerpoint transition
- create a video adding together these tweets on the chosen topin

## How to Use
Usage is simple. 
There are several core codes: 
- main.py
- twitter.py
- makeimage.py
- ffmpeg.py

Within main.py, there is a function processtwitter(). 
This is the only thing needed to call the API. 
For example: processtwitter(Boston) shall return a video called Boston.mp4. This video contains 3 most recent tweets regarding Boston. 
This video is within the /results folder. 
It also returns the images used to create the video. 

The project is written in Python. It relies heavily on the twitter API, ffmpeg and the PIL library. 
