import math, datetime as dt

class SimpleA:
	def __init__(self):
		print(self.__class__.__name__)

class SimpleB(SimpleA):
	"""docstring for SimpleB"""
	def __init__(self):
		super(SimpleB, self).__init__()
		print(self.__class__.__name__)

if __name__ == '__main__':
	print("Welcome to class inheritance")
	obj0 = SimpleA()
	print("How you see inherit classes ??")
	obj1 = SimpleB()
	print("Pi number is %.2f" % math.pi)
	print("----------------------")
	print(obj1.__doc__)
	print("----------------------")
	mySMSTemplate = """
Hello %(name)s,

Your electric invoice is %(total).2f TL.
Last payment date is: %(last_date)s.

Thank you
"""
	last_date = dt.datetime(2019, 4, 20)
	last_date = last_date.strftime("%d.%m.%Y") # We convert date as string in Turkish format
	mySMS = mySMSTemplate % dict(name="Burak", total=50.10145349, last_date=last_date)
	print(mySMS)
	input()