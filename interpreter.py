import nltk
from rippletagger.tagger import Tagger
from product import Product

LANG = 'portuguese'
LANG_CODE = 'pt-2'

def interpret(sender, message):
	tokens = tokenize(message)
	tokens = tag(tokens)
	products = identify_products(tokens)
	answer = ""
	if(len(products) > 0):
		for product in products:
			answer += str(product) + '?\n'
	else:
		answer = 'waaat?'
	return answer

def tokenize(message):
	return nltk.tokenize.word_tokenize(message, language=LANG)

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
