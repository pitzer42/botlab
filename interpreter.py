import nltk
from nltk import tokenize
from rippletagger.tagger import Tagger
from product import Product

LANG = 'portuguese'
LANG_CODE = 'pt-2'

def interpret(sender, message):
	tokens = tokenize.word_tokenize(message, language=LANG)
	tokens = tag(tokens)
	answer = ""
	for product in identify_products(tokens):
		answer += str(product) + '?\n'
	return answer

def tokenize_message(message):
	return tokenize.word_tokenize(message, language=LANG)

def tag(tokens):
	#RSLPStemmer uses xrange from python 2.7 and was the best POS tagger found.
	#this is a hack to replace all calls to xrange to range.
	__builtins__['xrange'] = range
	tagger = Tagger(language=LANG_CODE)
	return tagger.tag(' '.join(tokens))

def identify_products(tagged_tokens):
	product = None
	products = []
	for token, tag in tagged_tokens:
		if(tag == 'NOUN'):
			if(product):
				products.append(product)
			product = Product(token, [])
		elif(tag == 'ADJ'):
			if(product):
				product.attributes.append(token)
	if(product):
		products.append(product)
	return products
