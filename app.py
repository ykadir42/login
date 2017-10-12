#Jawadul Kadir and Kelly Wang
#SoftDev1 pd7
#HW8 -- Do I Know You?
#2017-10-04

from flask import Flask, render_template, request, session, redirect, url_for, flash
import os

app = Flask(__name__)

app.secret_key = os.urandom(32) #32 bits of random data as a string

#hardcoded login credentials
username = 'kelly'
password = 'wang'

@app.route("/")
def hello_world():
	if 'username' in session:
		return redirect(url_for("hello"))
	return redirect(url_for("form"))

@app.route("/form", methods=["POST", "GET"])
def form():
	if 'username' in session:
		return redirect(url_for("hello"))
	return render_template("form.html")

'''
@app.route("/error")
def error():
	if 'username' not in session:
	        return render_template("error.html", error = session['error'])
	return redirect(url_for("hello"))
'''

@app.route("/auth", methods=["POST"])
def auth():
	if 'username' in session:
		return redirect(url_for("hello"))
	print session;
	print '_______________________________________________COOKIES GET USERNAME'
	print request.cookies.get('username')
	print "-----------------------ARGS "
	print request.args
	print "-----------------------FORM "
	print request.form
	#checks if login credentials are correct
	if request.form["username"] == "kelly":
		if request.form['password'] == 'wang':
		    session['username'] = request.form['username']
		    print session
		    return redirect(url_for("hello"))
		else:
			flash('Wrong Password')
			return redirect(url_for('form'))
	else:
		flash('Wrong Username')
		return redirect(url_for('form'))

#welcome page
@app.route("/hello")
def hello():
        if 'username' not in session :
                return redirect(url_for("form"))
	return render_template("hello.html", username = session['username'])

#exit page
@app.route("/goodbye", methods=["POST"])
def goodbye():
	#logs out user
	session.pop('username')
	return redirect(url_for("form"))

        

if __name__ == "__main__":
	app.debug = True
	app.run()










