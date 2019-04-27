#!/usr/bin/python3
'''
Vector class that represt two-dimensional vectors.

Here we defined the __add__ method in Vector class to perform vector addition 
and then the plus operator would behalf as per expectation.
'''
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __str__(self):
		return "Vector (%d, %d)" % (self.a, self.b)
	def __add__(self, other):
		return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 4)
v2 = Vector(5, -6)
v3 = v1 + v2

print(v1)
print(v2)
print(v3)