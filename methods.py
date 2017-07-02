#Methods
class fighter(object):
	"""docstring for fighter"""
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage  = 10


	def attack(self, other):
		other.health -= self.damage
		print("{}: attacks {}!".format(self.name, other.name))
		print("{}: losses {} healht point!".format(other.name, self.damage))




	def __str__(self):    #String represenation
		return "{}: {}".format(self.name, self.health)




Frank = fighter("Frank")
James = fighter("James")

print(Frank)
print(James)

James.attack(Frank)
print(Frank)


