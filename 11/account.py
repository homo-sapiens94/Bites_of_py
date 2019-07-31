class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)
    
    def __add__(self, other):
        if type(other)!=int:
            raise ValueError
        self._transactions.append(other)
    
    def __sub__(self, other):
        if type(other)!=int:
            raise ValueError
        self._transactions.append(-other)
    
    def __lt__(self, other):
        if type(other)==int:
            return self.balance < other
        return self.balance < other.balance
    
    def __le__(self, other):
        if type(other)==int:
            return self.balance <= other
        return self.balance <= other.balance
    
    def __eq__(self, other):
        if type(other)==int:
            return self.balance==other
        
        return self.balance == other.balance    
    
    def __ge__(self, other):
        if type(other)==int:
            return self.balance >= other
    
        return self.balance >= other.balance 
    
    def __gt__(self, other):
        if type(other)==int:
            return self.balance>other
       
        return self.balance > other.balance    
        
    
    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'
        
    def __getitem__(self, key):
        return self._transactions[key]
            


            