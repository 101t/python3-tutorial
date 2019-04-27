#!/usr/bin/python3
print("Welcome to python3 calculator:")
while True:
	x = float(input("Please Enter first number: "))
	y = float(input("Please Enter second number: "))
	cmd = """
	[1] x + y
	[2] x - y
	[3] x * y
	[4] x / y
	[5] x % y
	[0] return
	"""
	print(cmd)
	z = input("Please select operator: ")

	try:
		if z == "1":
			print(x + y)
		elif z == "2":
			print(x - y)
		elif z == "3":
			print(x * y)
		elif z == "4":
			print(x / y)
		elif z == "5":
			print(x % y)
		else:
			pass
	except ZeroDivisionError as e:
		print(e)
	except TypeError as e:
		print(e)
	except Exception as e:
		print(e)
		#raise e
	zz = input("Do you want to continue [Y/n]: ")
	if zz == "n":
		break