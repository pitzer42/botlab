"""This is a hack to redirect calls for xrange to range. It is required because
RSLPStemmer uses xrange from python 2.7 and it is the best POS tagger found so far."""
__builtins__['xrange'] = range

import nltk
import botlab.config as config
from rippletagger.tagger import Tagger
from botlab.models import Topic
import requests

import json

def tokenize(text):
    return nltk.tokenize.word_tokenize(text, language=config.LANG)

def tag(tokens):
    tagger = Tagger(language=config.LANG_CODE)
    return tagger.tag(' '.join(tokens))

def topics_from_tags(tagged_tokens, sentiment=0.5):
    topic = None
    topics = []
    for token, tag in tagged_tokens:
        if(tag in config.TOPIC_KEY_TAGS):
            if(topic):
                topics.append(topic)
            topic = Topic(token, [], sentiment)
        elif(tag == config.ATTRIBUTE):
            if(topic):
                topic.attributes.append(token)
    if(topic):
        topics.append(topic)
    return topics

def topics_from_text(text):
    tokens = tokenize(text)
    tags = tag(tokens)
    sentiment = get_sentiment(text)
    return topics_from_tags(tags, sentiment)

def get_sentiment(text):
    headers = {'Ocp-Apim-Subscription-Key': config.AZURE_ACCESS_KEY}
    data = { 'documents': [
        { 'id': '1', 'language': config.AZURE_LANG_CODE, 'text': text },
    ]}
    data = json.dumps(data)
    response = requests.post(config.AZURE_TEXT_ANALYTICS_ENDPOINT, data=data, headers=headers)
    return response.json()['documents'][0]['score']
