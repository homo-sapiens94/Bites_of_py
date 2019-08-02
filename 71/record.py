class RecordScore():
    """Class to track a game's maximum score"""
    highest= 0

    def __call__(self, value):
    	if value > self.highest:
    		self.highest = value
    	return self.highest



record = RecordScore()
print(record(1))
record(10)
record(9)
print(record(11))
print(record.highest)  # initial max
record(5)
