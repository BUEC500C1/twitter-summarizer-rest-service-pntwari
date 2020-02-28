import pytest
import twitter
import makeimage
import main
import ffmpeg

def test_twitter():

  assert isinstance(twitter.gettweets("stock"), list)