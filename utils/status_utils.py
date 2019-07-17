import pickle
import re

# load list of dummy words
with open('~/statusDV/static/dummy_words', 'rb') as fh:
    DUMMY_DATA = pickle.load(fh) #global constant, list of dummy words


def dummy_status(max_words=2000):
	"""
	generates a random word-frequency dict
		Args:
			max_words (int, default=2000): max number of  word-frequency 
			pair to generate
		Returns:
			dict object which contains random words as its key and random 
			word count as its value.
	"""

	# generate random words from DUMMY_DATA, random ints between 1-1000
    sample_strs = np.random.choice(DUMMY_DATA, size=max_words, replace=False)
    sample_ints = np.random.randint(low=1, high=2000, size=max_words)
    return dict(zip(sample_strs, sample_ints))


def filter_words(words):
	"""
	removes non-ascii chars and extra white space from given string
		Args:
			words (str): string of words to filter
		Returns:
			filtered string with only ascii chars and single whitespace 
	"""
    return re.sub(r'[^\x00-\x7F]+', '',
           words.replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\\', ""))