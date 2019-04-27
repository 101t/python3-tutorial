from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello Falsk!!"

@app.route('/param/<name>')
def hello_name(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
	app.run()
