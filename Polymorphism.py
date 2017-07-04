# Polymorphism
class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name


	def talk(self):
		pass


class Dog(Animal):
	def talk(self):
		return "WOOF WOOF"


class Cat(Animal):
	def talk(self):
		return "MEOW MEOW"


pet1 = Dog("Remy")
print(pet1.name)
print(pet1.talk())

print("")
pet2 = Cat("Cynthia")
print(pet2.name)
print(pet2.talk())
		

