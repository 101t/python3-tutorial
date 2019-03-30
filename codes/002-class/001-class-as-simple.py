
class MyClass:
	def __init__(self):
		pass

class SimpleClass:
	def __init__(self):
		print("I am Simple Class")
	def __str__(self):
		return "Simple Class!!"

class SimpleClassArgs:
	def __init__(self, name, is_active=True):
		self.name = name
		self.is_active = is_active
	def get_name(self):
		return self.name
	def is_activated(self):
		return self.is_active
	def __str__(self):
		return self.__class__.__name__

if __name__ == '__main__':
	print("Welcome to Class as Simple")
	obj0 = MyClass()
	print(obj0)
	obj1 = SimpleClass()
	print(obj1)
	obj2 = SimpleClassArgs("Jone Doe", True)
	obj3 = SimpleClassArgs("Jone Doe", is_active=True)
	obj4 = SimpleClassArgs(name="Jone Doe", is_active=True)
	obj5 = SimpleClassArgs(is_active=True, name="Jone Doe")
	obj6 = SimpleClassArgs("Jone Doe")
	obj7 = SimpleClassArgs(name="Jone Doe")
	print(obj7)
	print("This is my name: ", obj7.get_name())
	print("This is my name: " + obj7.get_name())
	print("This is my name: %s" % obj7.get_name())
	print("This is my name: {}".format(obj7.get_name()))
	print("This is my name: {0}".format(obj7.get_name()))
	print("This is my name: {0}, my age is {1}".format(obj7.get_name(), 24))
	print("This is my name: %(name)s" % {"name": obj7.get_name()})
	print("This is my name: %(name)s" % dict(name=obj7.get_name()))
	print("This is my name: %(name)s, my age is %(age)d" % dict(name=obj7.get_name(), age=24))
	input()