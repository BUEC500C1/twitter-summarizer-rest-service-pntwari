#!/usr/bin/env python


def key_def():
	consumer_key = "NA"
	consumer_secret = "NA"
	access_key = "NA"
	access_secret = "NA"
	return [consumer_key, consumer_secret, access_key, access_secret]
	
if __name__ == '__main__':
    #pass in the username of the account you want to download
    #get_all_tweets("@BU_Tweets")
	key = key_def()
	print(key[1])
	
	
	