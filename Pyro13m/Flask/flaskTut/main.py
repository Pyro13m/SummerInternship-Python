from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "kkkk"

@app.route("/home")
def new():
	return render_template(
        'test.html')

@app.route('/login', methods=['post'])
def addRegion():
    return ("You are Logged in MR./MRs. "+ request.form['username'])