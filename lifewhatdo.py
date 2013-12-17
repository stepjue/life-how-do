#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Tweets random questions from Yahoo! Answers as @lifehowdo

from get_yahoo import Page
import tweepy, time, random

HOUR = 3600 # in seconds
MIN_SLEEP = HOUR / 2
MAX_SLEEP = 3 * HOUR

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
	newpost = page.get_random_question()
	api.update_status(newpost)
	print(newpost)

	# Sleeps between 30 minutes and 3 hours between tweets
	time.sleep(random.randrange(MIN_SLEEP, MAX_SLEEP))