# Flask-Login-App-Tutorial
Tutorial for how to make a simple Flask login app, with a SQLite3 database
All files are included
***
Hello, today I am going to teach you how to setup a Flask login page. 

First, you want to install virtual environment on your system. This can be done in the command line using pip install virtualenv.
Navigate the folder where you want flask to reside in, and in there enter the command pip install flask.
Next, you want to verify setup was correct, so let's create a Hello World app.

***
Create a file anywhere, I named mine __init__.py
In that anywhere, create two folders, static and templates.

__init__.py should contain the following code: 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return "Hello World"

if __name__== "__main__":
    app.run()
```

Next, you want to go to where you installed Flask, open the script directory in command prompt, and enter activate
From there, navigate to your __init__.py location, and then run it using python __init__.py 
In your browser, navigate to http://127.0.0.1:5000/ to verify that it worked.
The words Hello World should appear on your screen.
I found this video to be useful in the setup:

[![Flask Setup](https://i.ytimg.com/vi_webp/98JY6MvumVs/mqdefault.webp)](http://www.youtube.com/watch?v=98JY6MvumVs)
***
Now to create the login page. In order to do so, let's go back into __init__.py.
We need to add a route for login, so replace your index function with the following code: 
```python
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)
 ```

Let's make a template called login.html
It's contents will be: 
```html
<html>
  <head>
    <title>Flask Intro - login page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <h1>Please login</h1>
      <br>
      <form action="" method="post">
        <input type="text" placeholder="Username" name="username" value="{{
          request.form.username }}">
         <input type="password" placeholder="Password" name="password" value="{{
          request.form.password }}">
        <input class="btn btn-default" type="submit" value="Login">
      </form>
      {% if error %}
        <p class="error"><strong>Error:</strong> {{ error }}
      {% endif %}
    </div>
  </body>
</html>
```
Visit http://127.0.0.1:5000/login to verify that this works. Right now, the username and password is set to admin.
However, we don't have a destination yet, so let's add a secret route too!
```python  
@app.route('/secret')
def secret():
    return "This is a secret page!"
```
  You also need to update your imports, they are now: 
```python
  from flask import Flask, render_template, redirect, url_for, request
```
***
Now that you have seen a basic login system, let's setup a database. We will be using a SQLite3 database.
Open command prompt in your static directory and enter the following commands:
```cmd
$ sqlite3
$ User.db
$ CREATE TABLE USERS(USERNAME TEXT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL);
$ INSERT INTO USERS (USERNAME, PASSWORD)
$ VALUES ('your_username', 'your_password')
```
I used MD5 to store my passwords, and you should too. 
You can then use the module `hashlib to convert the user input password to this password, and increase your security.
What this does is create a database named User.db, and creates a Table of users in that database. It then creates a user, with a username and password of your choosing.
You can use your own passwords, or add as many as you would like.

Now we need to update our file to process SQL.
At the top, add an import for the python SQLite3 module.

```python
import sqlite3
```
```import hashlib``` If you want to use MD5 as well.

Also, you're going to have to rework your login method. It will now look like: 
```python
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html', error=error)
```
You are also going to need a method called validate to compare the values. 
```python
def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM Users")
                rows = cur.fetchall()
                for row in rows:
                    dbUser = row[0]
                    dbPass = row[1]
                    if dbUser==username:
                        completion=check_password(dbPass, password)
    return completion

```
It takes the inputed username and passwords as arguments, and compare them against the users table.

If you have your passwords stored as MD5, you'll have to convert the user input password as MD5. To do that, I created a method called check_password.

One of the username as password sets in the user.db database is Username: leet1337 Password: python
```python
def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

```
***
Your file structure will look like
```

--Main Folder
    --__init__.py
    --Static
        --user.db
    --Templates
        --login.html
```
        
Thanks for reading!
