class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		print 'I got a car!'
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12

	def display_all(self):
		print 'Price: {0!s}\nSpeed: {1!s}\nFuel: {2}\nMileage: {3!s}\nTax: {4!s}%'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)
		return self

my_car = Car(2000, 150, 'Empty', 670000)
my_car.display_all()

my_car = Car(20000, 200, 'Full Tank', 60000)
my_car.display_all()

my_car = Car(100, 80, 'Half Full', 6700000)
my_car.display_all()

my_car = Car(50000, 240, 'Half Empty', 70000)
my_car.display_all()