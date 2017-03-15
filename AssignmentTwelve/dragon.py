from animal import Animal

class Dragon(Animal):
	def __init__(self, name='Elliot'):
		self.name = name
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

dragon = Dragon()
dragon.walk().walk().walk().run().run().fly().fly().display_health()