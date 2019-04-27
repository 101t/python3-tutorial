from flask import Flask, redirect, url_for, request, render_template
import os

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
#print(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
	return "Hello Falsk!!"


@app.route('/hello/<name>')
def hello_name(name):
	return "Hello {}!".format(name)


@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		user = request.form["name"]
		return redirect(url_for("hello_name", name=user))
	else:
		# user = request.args.get("name", "Jone")
		# return redirect(url_for("hello_name", name=user))
		name = "Welcome to Flask Project"
		return render_template('login.html', name=name)

if __name__ == '__main__':
	app.run()
