from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')



d = feedparser.parse(FEED_URL)

def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    # lst = []
    # for item in d.entries:
    # 	game =Game(item.title,item.link)
    # 	lst.append(game)
    # print(lst)

    lst =[Game(item.title,item.link) for item in d.entries]
    print(lst)
get_games()