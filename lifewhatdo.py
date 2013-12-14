import feedparser # parses RSS feeds
import enchant # spellchecking library
import string

MAX_TWEET = 140
RSS_FEED = 'http://answers.yahoo.com/rss/allq'

dictionary = enchant.Dict('en_US')
exclude = set(string.punctuation)

class Post():
	def __init__(self, q):
		self.question = q
		self.score = caps_score()

	# scores a post based on the number of all-caps words it has
	def caps_score(self):
		caps_count = sum([(word.isupper() and len(word) > 4) \
			for word in self.question.split(' ')])
		if caps_count > 1:
			return 1
		else:
			return 0

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
			question = post[start:]
			posts.append(Post(question))
	return posts

def main():
	entries = get_entries()
	posts = process_entries(entries)
	for p in posts:
		print(p.question + ': CAPS = ' + str(p.caps_score()))

if __name__ == '__main__':
	main()