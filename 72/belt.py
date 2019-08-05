from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)

def get_belt(user_score):

    if user_score < MIN_SCORE:
    	return None
    elif user_score > MAX_SCORE:
    	return HONORS[MAX_SCORE]
    else:
    	if user_score in scores:
    		return HONORS[user_score]
    	else:
    		temp = 0
    		for value in scores:
    			if user_score - value>0:
    				temp = value
    			else:
    				break
    		return HONORS[temp]



#Pybites Solution

from collections import OrderedDict
from itertools import takewhile

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    """Bit more verbose but more readable?"""
    if user_score < MIN_SCORE:
        return None

    if user_score >= MAX_SCORE:
        return HONORS[MAX_SCORE]

    for start, end in zip(scores, scores[1:]):
        if start <= user_score < end:
            return HONORS[start]

    raise RuntimeError('should not reach')


def get_belt_itertools(user_score):
    """Using itertools.takewhile"""
    if user_score < MIN_SCORE:
        return None

    belts = takewhile(lambda x: x[0] <= user_score,
                      HONORS.items())
    return list(belts)[-1][1]



