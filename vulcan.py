from flask import Flask,render_comment
from flask.ext.script import Manage
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
app = Manage(app)

@route('/')
def index():
		pass

@route('/user/<name>')
def user(name):
	return "Hello,%s",%name

if __main__ == '__name__':
	manage.run()