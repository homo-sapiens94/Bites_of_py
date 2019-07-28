NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return [i.title() for i in list(set(NAMES))]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names  = [' '.join(name.split()[::-1]) for name in names]
    names = sorted(names, reverse=True)
    names  = [' '.join(name.split()[::-1]) for name in names]
    return names

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    
    shortest= names[0].split()[0]

    for i in names:
        if len(i.split()[0])<len(shortest):
            shortest = i.split()[0]
    return shortest
