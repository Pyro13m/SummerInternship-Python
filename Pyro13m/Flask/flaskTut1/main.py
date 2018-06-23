from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route("/")
def new():
	return render_template('test.html')
	#return render_template('test.html')


@app.route("/here", methods = ['POST'])
def next():
	return "You're Here!"
'''
@app.route('/login', methods=['POST'])
def login():
	error= None
	return render_template('login.html',error=error)
'''

if __name__== 'main':
	app.run(debug=True)