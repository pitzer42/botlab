import config
import requests

def url_for(item):
    url = config.SEARCH_URL_TEMPLATE.format(item)
    content = str(requests.get(url).content)
    if content.find(config.INVALID_CONTENT_SEQUENCE) == -1:
        return url
    return False
