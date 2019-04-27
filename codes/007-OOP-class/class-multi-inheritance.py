'''
Working with multiple inheritance to avoid using super() method for overloading A and B classes at same time
'''

class A:
	def __init__(self):
		print("I am class A")
class B:
	def __init__(self):
		print("I am class B")

class C(A, B):
	def __init__(self):
		B.__init__(self)
		A.__init__(self)
		print("I am class C")

c1 = C()
print(c1.__class__.__bases__)