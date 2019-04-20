import requests, json

print("Welcome to github API tester!!!")

username = input("Please Enter github username: ")

if not username:
	username = "101t"

url = "https://api.github.com/users/%(username)s" % dict(username=username)

res = requests.get(url)

loadeddata = json.loads(res.text)

print(json.dumps(loadeddata, indent=4, sort_keys=True))

print("=============== WHAT INSIDE HEADERS ============")
#print(json.dumps(res.headers.__dict__, indent=4, sort_keys=True))
for k, v in res.headers.items():
	print("{} {}".format(k, v))

input()