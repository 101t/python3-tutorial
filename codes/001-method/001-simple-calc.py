"""
Understanding Method usage
"""

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mult(a, b):
	return a * b

def dev(a, b):
	return a / b

def mod(a, b):
	return a % b

def power(a, b):
	return a ** b

if __name__ == '__main__':
	print("Welcome to calc")
	x = int(input("please enter first number: "))
	y = int(input("please enter second number: "))
	print("a + b = ", add(x, y))
	print("a - b = ", sub(x, y))
	print("a * b = ", mult(x, y))
	print("a / b = ", dev(x, y))
	print("a % b = ", mod(x, y))
	print("a ** b = ", power(x, y))
	input()