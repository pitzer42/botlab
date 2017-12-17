"""This is a hack to redirect calls for xrange to range. It is required because
RSLPStemmer uses xrange from python 2.7 and it is the best POS tagger found so far."""
__builtins__['xrange'] = range

import nltk
import config
import random
from rippletagger.tagger import Tagger
from product import Product
import requests

def interpret(sender, text):
	tokens = tokenize(text)
	tokens = tag(tokens)
	products = identify_products(tokens)
	product_urls = valid_product_urls(products)
	if(len(product_urls) > 0):
		return '\n\n'.join(answer)
	return random_answer()

def tokenize(text):
	return nltk.tokenize.word_tokenize(text, language=config.LANG)

def tag(tokens):
	tagger = Tagger(language=config.LANG_CODE)
	return tagger.tag(' '.join(tokens))

def identify_products(tagged_tokens):
	product = None
	products = []
	for token, tag in tagged_tokens:
		if(tag == config.NAME):
			if(product):
				products.append(product)
			product = Product(token, [])
		elif(tag == config.ATTRIBUTE):
			if(product):
				product.attributes.append(token)
	if(product):
		products.append(product)
	return products

def valid_product_urls(products):
	return [url for product in products if is_url_valid(product_url(product))]

def product_url(product):
	return config.SEARCH_URL_TEMPLATE.format(product.name)

def is_url_valid(url):
	content = str(requests.get(url).content)
	return content.find('o encontrou resultado') > -1

def random_answer():
	return random.choice(config.DEFAULT_ANSWERS)
