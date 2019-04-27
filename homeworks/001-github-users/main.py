#!/usr/bin/python3
import requests, json, os

def write_and_save():
	username = input("Please Enter github username: ")

	if not username:
		username = "101t"


	url = "https://api.github.com/users/%(username)s" % dict(username=username)

	res = requests.get(url)

	loadeddata = json.loads(res.text)

	payload = json.dumps(loadeddata, indent=4, sort_keys=True)

	with open('users/%(username)s.json' % dict(username=username), 'w+') as f:
		f.write(payload)
def read_saved():
	username = input("Please Enter github username: ")

	if not username:
		raise ValueError("No username entered")
	payload = ""
	with open('users/%(username)s.json' % dict(username=username), 'r+') as f:
		payload = f.read()
	print(payload)

def delete_user():
	username = input("Please Enter github username: ")

	if not username:
		raise ValueError("No username entered")
	os.remove('users/%(username)s.json' % dict(username=username))

if __name__ == '__main__':
	print("Welcome to github API tester!!!")
	while True:
		cmd = """
		[1] write and save Github username
		[2] read saved Github username
		[3] delete Github username
		[0] return
"""
		print(cmd)
		z = input("Please select one choice to continue: ")
		try:
			if z == "1":
				write_and_save()
			elif z == "2":
				read_saved()
			elif z == "3":
				delete_user()
			else:
				pass
		except Exception as e:
			print(e)
		zz = input("Do you want to continue [Y/n]: ")
		if zz == "n":
			break