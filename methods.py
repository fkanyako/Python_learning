#Methods

class Fighter(object):
	"""docstring for Fighter"""
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10


	def attack(self, other):
		other.health -= self.damage




	Frank = Fighter("Frank")
	James = Fighter("James")

	print(Frank.name)
	print(James.name)

	James.attack(Frank)

	print(Frank.health)
