from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:

    def __init__(self, name):
    	self.name = name
    	self._transactions = []
    	self.karma = 0
    	self._fans = []

    def __add__(self, other):
    	self._transactions.append(other.points)
    	self.karma += other.points
    	self._fans.append(other.giver)
    
    @property
    def points(self):
    	return self._transactions

    @property
    def fans(self):
    	return len(self._fans)
    
    
    def __str__(self):
    	if self.fans>1: 
    		return f'{self.name} has a karma of {self.karma} and {self.fans} fans'
    	else:
    		return f'{self.name} has a karma of {self.karma} and {self.fans} fan'

# alice = User('alice')
# bob = User('bob')
# tim = User('tim')


#Pybites solution
# class User:

#     def __init__(self, name):
#         self.name = name
#         self._transactions = []

#     def __add__(self, transaction):
#         self._transactions.append(transaction)

#     @property
#     def points(self):
#         return [tr.points for tr in self._transactions]

#     @property
#     def karma(self):
#         return sum(self.points)

#     @property
#     def fans(self):
#         return len({t.giver for t in self._transactions})

#     def __str__(self):
#         fan = self.fans == 1 and 'fan' or 'fans'
#         return f'{self.name} has a karma of {self.karma} and {self.fans} {fan}'


