import feedparser # parses RSS feeds
import string, random

RSS_FEED = 'http://answers.yahoo.com/rss/allq'
MAX_TWEET = 140
MAX_DIGITS = 8

class Post():
	def __init__(self, q):
		self.question = q
	
	def num_digits(self):
		return len([ch for ch in self.question if ch in string.digits])

def get_entries():
	d = feedparser.parse(RSS_FEED)
	entries = [post.title for post in d.entries]
	return entries

# creates a list of Post objects from the rss feed
def process_entries(entries):
	posts = []
	colon_len = len(' : ')
	for post in entries:
		start = post.find(' : ') + colon_len
		if len(post) <= MAX_TWEET:
			question = post[start:]
			posts.append(Post(question))
	return posts

def get_rand_post():
	entries = get_entries()
	posts = process_entries(entries)

	# remove posts with more than MAX_DIGITS digits
	posts = [p for p in posts if p.num_digits() < MAX_DIGITS]
	post_len = len(posts)
	rand_post = posts[random.randrange(0,post_len)].question
	return rand_post
