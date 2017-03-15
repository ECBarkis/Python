from animal import Animal

class Dog(Animal):
	def __init__(self, name='Snoopy'):
		self.name = name
		self.health = 150

	def pet(self):
		self.health += 5
		return self

dog = Dog('Snoop')
dog.walk().walk().walk().run().run().pet().display_health()