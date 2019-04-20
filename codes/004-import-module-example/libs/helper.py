"""
This is my library
Copyright MIT
Author Ahemt
version: 1.0
"""
import datetime as dt
import time

class Helper:
	"""This is my Helper class"""
	def __init__(self, *args, **kwargs):
		self.List = args
		self.Dict = kwargs

	def get_datetime(self):
		"""
		strptime: convert str => datetime obj
		strftime: convert datetime obj => str
		"""
		birthdate = self.Dict.get("birthdate")
		if birthdate:
			return dt.datetime.strptime(birthdate, "%d.%m.%Y")
		return

class MyPrivateClass:
	pass