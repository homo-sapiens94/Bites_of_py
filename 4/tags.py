import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET


# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()
    

# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    root = ET.fromstring(content)
    # root = tree.getroot()
    lst = []
    for category in root.iter('category'):
        lst.append(category.text)
    c = Counter(lst)
    return c.most_common(10)
    
    


#pybites solution

# import os
# import re
# from collections import Counter
# import urllib.request

# # prep
# TAG_HTML = re.compile(r'<category>([^<]+)</category>')

# tempfile = os.path.join('/tmp', 'feed')
# urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

# with open(tempfile) as f:
#     content = f.read().lower()


# # start coding

# def get_pybites_top_tags(n=10):
#     """use Counter to get the top 10 PyBites tags from the feed
#        data already loaded into the content variable"""
#     tags = TAG_HTML.findall(content)
#     return Counter(tags).most_common(n)