from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3 as sql
import hashlib

app = Flask(__name__)

def validate(username, password):
    conn = sql.connect('static/main.db')
    completion = False
    cursor = conn.cursor()
    if username == "" or password == "":
        pass
    else:
        cursor.execute("SELECT * FROM `student_table` WHERE `username` = ? AND `password` = ?", (username, password))
        if cursor.fetchone() is not None:
            completion = True
        else:
            pass
    return completion

    


@app.route('/', methods=['GET', 'POST'])
def final():
    error = None
    username = request.form.get('username')
    password = request.form.get('password')
    completion = validate(username, password)
    if completion == False:
        print "comple-false"
        error = 'Invalid Credentials. Please try again.'
    else:
        return redirect(url_for('secret'))
        print "comple-true"
    return render_template('final1.html', error=error)

@app.route('/secret')
def secret():
    #return "You have successfully logged in"
    return render_template(
    'success.html')
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run()
"""



from flask import Flask, render_template, request
app = Flask(__name__)
completion = False

def validate(username, password):
    conn = sql.connect('static/main.db')
    completion = False
    cursor = conn.cursor()
    if username == "" or password == "":
        pass
    else:
        cursor.execute("SELECT * FROM `student_table` WHERE `username` = ? AND `password` = ?", (username, password))
        if cursor.fetchone() is not None:
            completion = True
        else:
            pass
    return completion

@app.route('/')
def final():
   return render_template('final.html')

@app.route('/success',methods = ['POST', 'GET'])
def success():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion == False:
            return render_template("final.html",error="INVALID CREDENTIALS!!!")
        else:
            return render_template("success.html")


if __name__ == '__main__':
   app.run()

"""

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('final.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    conn = sql.connect('static/main.db')
    completion = False
    username = request.form['password']
    password = request.form['username']
    cursor = conn.cursor()
    if username == "" or password == "":
        flash('fill something')
    else:
        cursor.execute("SELECT * FROM `student_table` WHERE `username` = ? AND `password` = ?", (username, password))
        if cursor.fetchone() is not None:
            session['logged_in'] = True
        else:
            flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run()

