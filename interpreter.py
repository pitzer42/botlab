import pickle
import nltk
from nltk import tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

tagger = pickle.load(open("tagger.pkl"))
portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")

def interpret(sender, message):
    sentences = portuguese_sent_tokenizer.tokenize(text)
    tagged_words = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
    answer = []
    for word, tag in tagged_words:
        if (tag.startswith('NN')):
            answer.append(word)
    return ' '.join(answer) + '?'
