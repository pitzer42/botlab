import nltk
from nltk import tokenize

LANG = 'portuguese'

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(message, language=LANG)
    tokens = remove_stopwords(tokens)
    return ' '.join(tokens)

def remove_stopwords(tokens):
    stop_words = set(nltk.corpus.stopwords.words(LANG))
    return [token for token in tokens if not token in stop_words]
