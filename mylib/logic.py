import wikipedia


def wiki(name="funny", length=1):
    """I am coming from wikipedia"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
