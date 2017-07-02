#Methods
class fighter(object):
	"""docstring for fighter"""
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage  = 10


	def attack(self, other):
		other.health -= self.damage






Frank = fighter("Frank")
James = fighter("James")


print(Frank.name)
print(James.name)

James.attack(Frank)
print(Frank.health)


