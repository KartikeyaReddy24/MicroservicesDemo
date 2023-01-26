import wikipedia


def wiki(name="war goddess", length=1):
    """I am coming from wikipedia"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
