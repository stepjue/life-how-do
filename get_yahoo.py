import feedparser # parses RSS feeds
from enchant.checker import SpellChecker # spellchecking library
import string
import random

MAX_TWEET = 140
RSS_FEED = 'http://answers.yahoo.com/rss/allq'
MAX_DIGITS = 8

checker = SpellChecker('en-US')
exclude = set(string.punctuation)
digits = '0123456789'

class Post():
	def __init__(self, q, topic):
		self.topic = topic
		self.question = q
		self.score = self.caps_score() + self.spell_score()

	# scores a post based on the number of all-caps words it has
	def caps_score(self):
		caps_count = sum([(word.isupper() and len(word) > 4) \
			for word in self.question.split(' ')])
		if caps_count > 1:
			return 1
		else:
			return 0

	# scores a post based on the number of mispellings
	def spell_score(self):
		checker.set_text(self.question)
		count = len([err for err in checker])
		return count

	def num_digits(self):
		return len([ch for ch in self.question if ch in digits])

def get_entries():
	d = feedparser.parse(RSS_FEED)
	entries = [post.title for post in d.entries]
	return entries

def process_entries(entries):
	posts = []
	colon_len = len(' : ')
	for post in entries:
		is_open = post.find(' : ')
		if is_open and len(post) <= MAX_TWEET:
			start = is_open + colon_len
			topic = post[:is_open]
			question = post[start:]
			posts.append(Post(question, topic))
	return posts

def main():
	entries = get_entries()
	posts = process_entries(entries)
	posts.sort(key = lambda x: x.score, reverse = True)
	posts = [p for p in posts if p.num_digits() < MAX_DIGITS]
	lucky_post = posts[random.randrange(0,6)].question
	print(lucky_post)

if __name__ == '__main__':
	main()