import nltk
from nltk import tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def interpret(sender, message):
    tokens = tokenize.word_tokenize(message, language='portuguese')
    tagged_words = nltk.pos_tag(tokens)
    answer = []
    for word, tag in tagged_words:
        if (tag.startswith('NN')):
            answer.append(word)
    return ' ou '.join(answer) + '?'
