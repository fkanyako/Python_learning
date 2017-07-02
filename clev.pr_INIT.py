#First lesson on OOP python from Clever Programmer Qazi

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age


James = Student("James", 85, 26)
Fati = Student("Fatimata", 70, 19)


print(James.name)
print(Fati.name)
		

print(James.grade)
print(Fati.grade)

print(James.age)
print(Fati.age)

		