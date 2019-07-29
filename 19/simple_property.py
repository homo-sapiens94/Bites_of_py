from datetime import datetime,timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
    	self.name=name
    	self.expires=expires
    @property
    def expired(self):
    	return NOW>self.expires


past_time = NOW + timedelta(days=1)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired)
