import datetime as dt

class A:
	def __init__(self):
		print("Hi class A")
	def __str__(self):
		return "I am Class A"
	def __value(self): # This is private method
		return "I am Tarek"
	@property
	def value(self):
		return self.__value()
	
class B:
	def __init__(self):
		print("Hi class B")
	def __str__(self):
		return "I am Class B"

class PrintMyBirthday(B, A):
	"""docstring for PrintMyBirthday"""
	def __init__(self, birthday):
		self.a = A
		self.b = B
		self.birthday = birthday
	def get_mybirthday_as_string(self):
		return "Your birthdate in: %s" % self.birthday.strftime("%d.%m.%Y")
if __name__ == '__main__':
	bb = PrintMyBirthday(dt.datetime(1989, 3, 1))
	print("Hi All")
	a_obj = bb.a()
	print(a_obj.value)
	print(bb.get_mybirthday_as_string())
	input()