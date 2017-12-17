import nltk
from nltk import tokenize
from nltk.stem import RSLPStemmer
from rippletagger.tagger import Tagger

LANG = 'portuguese'
LANG_CODE = 'pt-2'

nltk.download('stopwords')
nltk.download('rslp')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(message)#, language=LANG)
    #tokens = remove_stopwords(tokens)
    tokens = tag(tokens)
    tokens = keep_tagged_tokens('NOUN', tokens)
    return ' ou '.join(tokens) + '?'

def keep_tagged_tokens(tag, tagged_tokens):
    result = []
    for i in tagged_tokens:
        if(i[1] == tag):
            print(i)
            result.append(i[0])
    return result

def tag(tokens):
    #RSLPStemmer uses xrange from python 2.7 and was the best POS tagger found.
    #this is a hack to replace all calls to xrange to range.
    __builtins__['xrange'] = range
    tagger = Tagger(language=LANG_CODE)
    return tagger.tag(' '.join(tokens))

def stem(tokens):
    stemmer = RSLPStemmer()
    return stemmer.stem(tokens)

def remove_stopwords(tokens):
    stop_words = set(nltk.corpus.stopwords.words(LANG))
    return [token for token in tokens if not token in stop_words]
