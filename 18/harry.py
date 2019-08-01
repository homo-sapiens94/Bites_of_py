import os
import urllib.request
from string import punctuation
import codecs
# data provided
# stopwords_file = os.path.join('/tmp', 'stopwords')
# harry_text = os.path.join('/tmp', 'harry')
# urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
# urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with codecs.open('stopwords.txt', 'r', encoding='utf-8',errors='ignore') as f:
        stop = f.read().split()
    # print(stop)
    with codecs.open('harry.txt', 'r', encoding='utf-8',errors='ignore') as f:
        harry = f.read().split()
    # print(harry)
    dict = {}
    
    for word in harry:
        word = word.strip(punctuation).lower()
        if not word.isalnum():
            continue
        elif word in stop:
            continue
        else:

            if word in dict:
                
                dict[word] += 1
            else:
                dict[word] = 1
    # print(dict)
    inverse = [(value, key) for key, value in dict.items()]            
    
    return (max(inverse)[1],max(inverse)[0])   

