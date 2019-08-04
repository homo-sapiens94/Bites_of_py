from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    lst = []
    c = Counter()
    for value in data:
    	if value['year'] == year:
    		lst.append(value['automaker'])
    return Counter(lst).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    final_value =set()
    for value in data:
    	if value['automaker'] == automaker and value['year'] == year:
    		final_value.add(value['model'])
    return final_value		
    		
    		
    		

#Pybites Solution
from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    cnt = Counter(row["automaker"] for row in data
                  if row["year"] == year).most_common()
    return cnt[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set([row["model"] for row in data
                if row["automaker"] == automaker and
                row["year"] == year])

                