class Animal(object):
	def __init__(self, name='I have no name'):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print 'Health: {0!s}'.format(self.health)
		return self

	def say_name(self):
		print self.name

# animal = Animal('animal')
# animal.walk().walk().walk().run().run().display_health()