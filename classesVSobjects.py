#Classes vs Objects

class Salone(object):
	"""docstring for Salone"""
	def __init__(self, city, population):
		self.city = city
		self.population = population



Freetown = Salone("Freetown", 1500000)
Bo = Salone("Bo", 450000)
kenema = Salone("Kenema", 250000)


print(Freetown.city)
print(Freetown.population)
print("")

print(Bo.city)
print(Bo.population)


#In this example, Salone is the class,
# def__init__ is the method
#name is the arttribute
#and Freetown, Bo, Kenema, are the objects
