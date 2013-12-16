#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Tweets random/stupid/funny questions from Yahoo! Answers

from get_yahoo import Page
import tweepy, time, random

HOUR = 3600 # in seconds

CONSUMER_KEY = 'xxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	page = Page()
	newpost = page.get_random_post()
	print newpost
	api.update_status(newpost)

	# sleeps between 30 minutes and 3 hours between tweets
	time.sleep(random.randrange(HOUR/2, 3*HOUR))