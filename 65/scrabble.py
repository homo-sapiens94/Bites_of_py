import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    all_words= _get_permutations_draw(draw)
    dic_words = []   
    for word in all_words:
    	if word in dictionary:
    		dic_words.append(word)
    
    return dic_words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    possible_words = []
    for i  in range(len(draw)):
    	for value in itertools.permutations(draw,i+1):
    		possible_words.append(''.join(value).lower())
    
    return possible_words
