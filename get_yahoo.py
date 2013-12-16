#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by stepjue

# Parses the Yahoo! Answers RSS feed, returns a random post

import feedparser	# for parsing the RSS feed
import string		# for Post.get_num_digits()
import random 		# for Page.get_random_post()

RSS_FEED = 'http://answers.yahoo.com/rss/allq'

MAX_TWEET = 140
MAX_DIGITS = 8
COLON_LEN = len(' : ')

# An object that represents an individual post.
class Post(object):

	# A post is initialized with a title, the part of the title that's the question,
	# the length of the question, and the number of digits in the question.
	def __init__(self, title):
		self.title = title
		self.question = self.get_question()
		self.length = self.get_length()
		self.num_digits = self.get_num_digits()
	
	def get_num_digits(self):
		return len([ch for ch in self.question if ch in string.digits])

	def get_length(self):
		return len(self.question)

	def get_question(self):
		start = self.title.find(' : ') + COLON_LEN
		return self.title[start:]

	# Twitter doesn't allow tweets over 140 characters.
	def is_tweetable(self):
		return self.length <= MAX_TWEET

	# Spam posts tend to have a bunch of numbers in them, so if there are more
	# than 8 digits, I'm marking the post as spam.
	def is_spam(self):
		return self.num_digits > MAX_DIGITS

# An object that represents a list of tweetable posts.
class Page(object):
	def __init__(self):
		self.posts = self.get_posts()
		self.num_posts = len(self.posts)

	# Returns a list of Post objects scraped from the titles of
	# the entries in the Yahoo! Answers RSS feed.
	def get_posts(self):
		d = feedparser.parse(RSS_FEED)
		posts = []
		for post in d.entries:
			p = Post(post.title)
			if p.is_tweetable() and not p.is_spam():
				posts.append(p)
		return posts

	# Grabs a random post from the page
	def get_random_post(self):
		return self.posts[random.randrange(0,self.num_posts)].question