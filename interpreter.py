import nltk
from nltk import tokenize
from nltk.stem import RSLPStemmer
from rippletagger.tagger import Tagger

LANG = 'portuguese'
LANG_CODE = 'pt-2'

nltk.download('punkt')
nltk.download('rslp')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(message, language=LANG)
    tokens = tag(tokens)
    tokens = keep_tagged_tokens('NOUN', tokens)
    return ' ou '.join(tokens) + '?'

def tag(tokens):
	#RSLPStemmer uses xrange from python 2.7 and was the best POS tagger found.
	#this is a hack to replace all calls to xrange to range.
	__builtins__['xrange'] = range
	tagger = Tagger(language=LANG_CODE)
	return tagger.tag(' '.join(tokens))

def keep_tagged_tokens(tag, tagged_tokens):
	return [token for token, token_tag in tagged_tokens if token_tag == tag]
