def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    s  = set()
    for value in programmers.values():
        if s:
            s = s.intersection(set(value))
        else:
            s.update(value)
    
    return (list(s))



#pybites Solution

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    languages = [set(language) for language in programmers.values()]
    return set.intersection(*languages)