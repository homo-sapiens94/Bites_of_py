from collections import Counter
def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return Counter(text.rstrip())[' ']






#Pybites Solution
# def count_indents(text):
#     """Takes a string and counts leading white spaces, return int count"""
#     # originally I had:
#     # import re
#     # re.split('\S', s)[0].count(' ')
#     # but this is more elegant (credit: https://stackoverflow.com/a/13241465)
#     return len(text) - len(text.lstrip())