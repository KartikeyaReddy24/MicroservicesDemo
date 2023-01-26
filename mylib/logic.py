import wikipedia
from textblob import TextBlob


def wiki(name="funny", length=1):
    """I am coming from wikipedia"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """I am coming from search wiki"""

    results = wikipedia.search(name)

    return results


def phrase(name):
    """Returns phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
