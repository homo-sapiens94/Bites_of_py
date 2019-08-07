import string
from itertools import cycle

def sequence_generator():
    sequence=[]
    for num,letter in zip(range(1,27),string.ascii_uppercase):
        sequence.extend([num,letter])
    return cycle(lst)
    
    

#pybites Solution


from itertools import cycle
from string import ascii_uppercase


def sequence_generator():
    numbers = cycle(range(1, len(ascii_uppercase) + 1))
    letters = cycle(ascii_uppercase)

    for number, letter in zip(numbers, letters):
        yield number
        yield letter