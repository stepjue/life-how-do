#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Tweets random/stupid/funny questions from Yahoo! Answers

import get_yahoo
import tweepy, time

HOUR = 3600 # in seconds

CONSUMER_KEY = 'xxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	newpost = get_yahoo.get_rand_post()
	print newpost
	api.update_status(newpost)
	time.sleep(HOUR)