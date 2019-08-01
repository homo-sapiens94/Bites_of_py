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


# Pybites solution using counter and 
# from collections import Counter
# import os
# import re
# import urllib.request

# stopwords_file = os.path.join('/tmp', 'stopwords')
# harry_text = os.path.join('/tmp', 'harry')
# urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
# urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


# def get_harry_most_common_word():
#     with open(stopwords_file) as f:
#         stopwords = set(f.read().strip().lower().split('\n'))

#     with open(harry_text) as f:
#         words = [re.sub(r'\W+', r'', word)  # [^a-zA-Z0-9_]
#                  for word in f.read().lower().split()]

#         words = [word for word in words if word.strip()
#                  and word not in stopwords]

#         cnt = Counter(words)
#         return cnt.most_common(1)[0]
