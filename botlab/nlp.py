"""This is a hack to redirect calls for xrange to range. It is required because
RSLPStemmer uses xrange from python 2.7 and it is the best POS tagger found so far."""
__builtins__['xrange'] = range

import nltk
import botlab.config as config
from rippletagger.tagger import Tagger
from botlab.product import Product
import requests

def tokenize(text):
    return nltk.tokenize.word_tokenize(text, language=config.LANG)

def tag(tokens):
    tagger = Tagger(language=config.LANG_CODE)
    return tagger.tag(' '.join(tokens))

def products_from_tags(tagged_tokens):
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

def products_from_text(text):
    tokens = tokenize(text)
    tags = tag(tokens)
    return products_from_tags(tags)
