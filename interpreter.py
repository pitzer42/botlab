import nltk
from nltk import tokenize

nltk.download('punkt')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(text, language='portuguese')
    return tokens[0]
