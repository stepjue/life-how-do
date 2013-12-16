import feedparser # parses RSS feeds
import string, random

RSS_FEED = 'http://answers.yahoo.com/rss/allq'
MAX_TWEET = 140
MAX_DIGITS = 8

COLON_LEN = len(' : ')

# An object that represents an individual post
class Post(object):
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

	def is_tweetable(self):
		return self.length <= MAX_TWEET

	def is_probably_not_spam(self):
		return self.num_digits < MAX_DIGITS

# an object that represents a list of tweetable posts
class Page(object):
	def __init__(self):
		self.posts = self.get_posts()
		self.num_posts = len(self.posts)

	def get_posts(self):
		d = feedparser.parse(RSS_FEED)
		posts = []
		for post in d.entries:
			p = Post(post.title)
			if p.is_tweetable() and p.is_probably_not_spam():
				posts.append(p)
		return posts

	def get_random_post(self):
		return self.posts[random.randrange(0,self.num_posts)].question