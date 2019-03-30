"""
Understaning IF-ELIF-ELSE statements
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
	print("1 => a + b")
	print("2 => a - b")
	print("3 => a * b")
	print("4 => a / b")
	print("5 => a % b")
	print("6 => a ** b")
	opr = str(input("please choose operator: "))
	if opr == "1":
		print("Result: %s" % add(x, y))
	elif opr == "2":
		print("Result: %s" % sub(x, y))
	elif opr == "3":
		print("Result: %s" % mult(x, y))
	elif opr == "4":
		print("Result: %s" % dev(x, y))
	elif opr == "5":
		print("Result: %s" % mod(x, y))
	elif opr == "6":
		print("Result: %s" % power(x, y))
	else:
		print("Operator does not match")
	input()

