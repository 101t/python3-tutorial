'''
This is Base Overloading Method example
'''

class Class1:
	def __init__(self):
		pass
	def __del__(self):
		print("I destroyed Oop!")

c1 = Class1()
print(dir(c1))
del c1