#from libs.helper import Helper
from libs import *

if __name__ == '__main__':
	bb = Helper()
	bb = Helper(1,2,3,4, name="Ahmet", birthdate="01.03.1991")
	print(help(Helper))
	print(bb.get_datetime())