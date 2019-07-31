import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    lst = []
    with open(DICTIONARY, "r") as file: 
        data = file.readlines() 
        for line in data: 
            word = line.strip() 
            lst.append(word) 
    return lst

def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    value = 0
    for letter in word:
        if letter.capitalize() not in LETTER_SCORES:
            return 0
        value += LETTER_SCORES[letter.capitalize()]
    return value


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    highest_score= calc_word_value(words[0])
    word_ = words[0]
    for word in words:
        current = calc_word_value(word)
        if current> highest_score:
            word_ = word
            highest_score = current
    return  word_










#Pybits solution
# def load_words():
#     """load the words dictionary (DICTIONARY constant) into a list and return it"""
#     with open(DICTIONARY) as f:
#         return [word.strip() for word in f.read().split()]


# def calc_word_value(word):
#     """given a word calculate its value using LETTER_SCORES"""
#     return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

# def max_word_value(words=None):
#     """given a list of words return the word with the maximum word value"""
#     if words is None:
#         words = load_words()
#     return max(words, key=calc_word_value)





