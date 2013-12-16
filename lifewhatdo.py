#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Tweets random questions from Yahoo! Answers as @lifehowdo

from get_yahoo import Page
import tweepy, time, random

HOUR = 3600 # in seconds

# Twitter keys for OAuth
CONSUMER_KEY = 'xxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxx'

# Authenticate as @lifehowdo
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# The main loop that tweets questions
while True:
	page = Page()
	newpost = page.get_random_post()
	api.update_status(newpost)

	# Just for debugging
	print(newpost)

	# Sleeps between 30 minutes and 3 hours between tweets
	time.sleep(random.randrange(HOUR/2, 3*HOUR))