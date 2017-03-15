class bike(object):
	def __init__(self, price, max_speed):
		print 'I got a new bike'
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def display_info(self):
		print 'Price - {0!s}\nMax Speed - {1!s}\nMiles - {2!s}'.format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print 'Riding'
		self.miles += 10
		return self

	def reverse(self):
		print 'Reversing'
		self.miles -= 5
		return self

me_bike = bike(200, 45)
me_bike.ride().ride().ride().reverse().display_info()

myself_bike = bike(400, 60)
myself_bike.ride().ride().reverse().reverse().display_info()

I_bike = bike(800, 80)
I_bike.reverse().reverse().reverse().display_info()