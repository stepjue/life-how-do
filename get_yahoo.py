#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Parses the Yahoo! Answers RSS feed, returns a random question

import feedparser  # for parsing the RSS feed
import string      # for string.digits and string.isalnum()
import random      # for Page.get_random_post()

MAX_TWEET = 140
MAX_DIGITS = MAX_SPECIAL_CHARS = 8
COLON_LEN = len(' : ')

rss_feed = 'http://answers.yahoo.com/rss/allq'

# An individual Yahoo! Answers post.
class Post(object):
	def __init__(self, title):
		self.title = title
		self.question = self.get_question()
		self.length = len(self.question)
	
	# Finds the colon in "[ <Category> ] : <Question>" and extracts the question
	def get_question(self):
		start = self.title.find(' : ') + COLON_LEN
		return self.title[start:]

	# Twitter doesn't allow tweets over 140 characters.
	def is_tweetable(self):
		return self.length <= MAX_TWEET

	# I'm defining spam as a question with more than 8 digits and/or special characters
	def is_spam(self):
		num_digits = num_special_chars = 0
		for char in self.question:
			if char in string.digits:
				num_digits += 1
			if not char.isalnum():
				num_special_chars += 1

		return (num_digits > MAX_DIGITS) or (num_special_chars > MAX_SPECIAL_CHARS)

# A list of tweetable Yahoo! Answers questions.
class Page(object):
	def __init__(self):
		self.posts = self.get_posts()
		self.num_posts = len(self.posts)

	# Returns a list of Post objects scraped from the titles of
	# the entries in the Yahoo! Answers RSS feed.
	def get_posts(self):
		d = feedparser.parse(rss_feed)
		posts = []
		for entry in d.entries:
			post = Post(entry.title)
			if post.is_tweetable() and not post.is_spam():
				posts.append(post)
		return posts

	# Grabs a random question from the page
	def get_random_question(self):
		random_post_index = random.randrange(0, self.num_posts)
		random_post = self.posts[random_post_index]
		return random_post.question