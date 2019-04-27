#!/usr/bin/python3

def divider():
	print("="*30)

class Employee:
	employee_count = 0
	def __init__(self, name, salary):
		self.name 	= name
		self.salary = salary
		Employee.employee_count += 1
	@classmethod
	def employeeCount(cls):
		print("Total Employee %d" % cls.employee_count)
	def __str__(self):
		return "Name: %(name)s\t\tSalary: %(salary)s" % dict(name=self.name, salary=self.salary)

emp1 = Employee("Ahmet", 2000)
emp2 = Employee("Sara", 3000)

print(emp1)
print(emp2)

divider()

Employee.employeeCount()

divider()

if not hasattr(emp1, 'age'):
	setattr(emp1, 'age', 30)
	age = getattr(emp1, 'age')
	print("Employee Age is", age)
	print(emp1.__dict__)
	delattr(emp1, 'age')
	print(emp1.__dict__)
