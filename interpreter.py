import nltk
from nltk import tokenize
from rippletagger.tagger import Tagger

LANG = 'portuguese'
LANG_CODE = 'pt-2'

nltk.download('punkt')
nltk.download('rslp')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(message, language=LANG)
    tokens = tag(tokens)
    return ' ou '.join(tokens) + '?'

def tokenize_message(message):
	return tokenize.word_tokenize(message, language=LANG)

def tag(tokens):
	#RSLPStemmer uses xrange from python 2.7 and was the best POS tagger found.
	#this is a hack to replace all calls to xrange to range.
	__builtins__['xrange'] = range
	tagger = Tagger(language=LANG_CODE)
	return tagger.tag(' '.join(tokens))

def identify_products(tagged_tokens):
	NOUN = 'NOUN'
	ADJ = 'ADJ'
	iterator = iter(tagged_tokens)
	products = []
	name, attributes, product = None
	item = iterator.next()
	while(item):
		identify_noun()
		identify_attributes()
		product = Product(name, attributes)
		products.append(product)
		move()

	def move():
		name, attributes, product = None
		item = iterator.next()

	def identify_noun():

		while(item is not None):
			if(item[1] == NOUN)
				identify_attributes()
				products.append(Product(noum, attributes))

	def identify_attributes():
		item = iterator.next()
		while(item is not None):
			if(item[1] == ADJ):
				attributes.append(item[0])


class Product:

	def __init__(self, name, *attributes):
		self.name = name
		self.attributes = attributes
