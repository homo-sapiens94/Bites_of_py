from itertools import permutations, combinations

friends = 'Bob Dante Julian Martin'.split()

def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
    	team = list(permutations(friends,team_size))
    else:
    	team = list(combinations(friends,team_size))
    
    return(team)




#Pybites Solution


import itertools


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        func = itertools.permutations
    else:
        func = itertools.combinations
    return func(friends, team_size)
