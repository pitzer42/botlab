import nltk
from nltk import tokenize

LANG = 'portuguese'

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")

def interpret(sender, message):
    tokens = tokenizer.tokenize(text, language=LANG)
    tagged_words = nltk.pos_tag(tokens, language=LANG)
    tagged_words = remove_stopwords(tagged_words)
    #answer = [word for word, tag in tagged_words if tag.startswith('NN')]
    #return ' '.join(answer) + '?'
    return ' '.join(tagged_words)

def remove_stopwords(tokens):
    stop_words = set(nltk.corpus.stopwords.words(LANG))
    return [token for token in tokens if not token in stop_words]
