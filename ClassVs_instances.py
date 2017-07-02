#Class vs.Instance variable

class Bestblog(object):

	website = "http://www.greenafricanow.com/"
	def __init__(self, name):
		self.name = name




Blog = Bestblog("VickieRemoe_blog")

print(Blog.name)   #Object_name.method
print(Bestblog.website) #Class_name.method





