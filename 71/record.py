class RecordScore():
    """Class to track a game's maximum score"""
    highest= 0

    def __call__(self, value):
    	if value > self.highest:
    		self.highest = value
    	return self.highest



    	