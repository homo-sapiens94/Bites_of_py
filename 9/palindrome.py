"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word = ''.join(ch for ch in word if ch.isalnum()).lower()
    return  word == word[::-1]

def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    longest_palindrome = ''
    if words is None:
        words = load_dictionary() 
    for word in words:
        if is_palindrome(word):
            if len(word)>len(longest_palindrome):
                longest_palindrome = word 

    return longest_palindrome



#pybites Solution

"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import re
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word = re.sub(r'\W+', '', word.lower())
    return word == word[::-1]


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if not words:
        words = load_dictionary()
    palindromes = (word for word in words if is_palindrome(word))
    return max(palindromes, key=len)