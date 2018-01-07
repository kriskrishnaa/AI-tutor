from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3 as sql
import hashlib
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)


@app.route('/')
def student():
   return render_template('final.html')

@app.route('/success',methods = ['POST', 'GET'])
def success():
   if request.method == 'POST':
      result = request.form
      conn = sql.connect('static/main.db')
      cursor = conn.cursor()
      username = request.form.get('username')
      password = request.form.get('password')
      print username
      print password
      cursor.execute("SELECT * FROM `student_table` WHERE `username` = ? AND `password` = ?", (username, password))
      if cursor.fetchone() is not None:
          return render_template("articlesmodified1.html")

@app.route('/article')
def article():
    return render_template('article.html')

@app.route('/iv')
def iv():
   return render_template('iv.html')

@app.route('/ke')
def ke():
    return render_template('ke.html')

@app.route('/acc')
def acc():
    return render_template('acc.html')

@app.route('/ia')
def ia():
    return render_template('ia.html')

@app.route('/rv')
def rv():
    return render_template('rv.html')

@app.route('/ia/nltkk',methods = ['POST', 'GET'])
def nltkk():
   if request.method == 'POST':
      user_text1 = request.form.get('user_text1')
      user_text2 = request.form.get('user_text2')
      user_text2 = str(user_text2)
      user_text1 = str(user_text1)

      vect = TfidfVectorizer(min_df=1)
      tfidf1 = vect.fit_transform(["Average acceleration is the change in velocity divided by an elapsed time.",
                             "Acceleration is the rate of change for velocity, that is, change in velocity over a specified period of time.Average acceleration is the final velocity minus the initial velocity per time taken",
                             " When a body is moving with variable acceleration, then its average acceleration in a given interval of time is defined as the ratio of the change in velocity of the body.",
                             user_text2])
      tfidf2 = vect.fit_transform(["A derivative is a contract between two parties which derives its value/price from an underlying asset. The most common types of derivatives are futures, options, forwards and swaps.",
                             "A derivative is a rate of change, which, geometrically, is the slope of a graph. In physics, velocity is the rate of change of position, so mathematically velocity is the derivative of position. Acceleration is the rate of change of velocity, so acceleration is the derivative of velocity.",
                             "a derivative is a rate of change, or graphically, the slope of the tangent line to a graph.",
                             user_text1])

      t1 = tfidf1 * tfidf1.T
      t2 = tfidf2 * tfidf2.T
      c1=t1.tocoo()
      c2 =t2.tocoo()
      x1 = np.ones((4,4))
      x2 = np.ones((4,4))
      x1[c1.row, c1.col]=c1.data
      x2[c2.row, c2.col]=c2.data
      #print x[c.row, c.col]
      g1 = x1[c1.row, c1.col]
      g2 = x2[c2.row, c2.col]
      av1 = (g1[0]+g1[4]+g1[8])/3
      print av1
      av2 = (g2[0]+g2[4]+g2[8])/3
      print av2
      if av1*100 > 40:
         print "bright"
      elif av1*100 > 22 and av1*100 < 40:
         print "average"
         return render_template("video.html")
      else:
         print "weak"
         return render_template("video.html")
      if av2*100 > 40:
         print "bright"
      elif av2*100 > 22 and av2*100 < 40:
         print "average"
         return """
         <h1>Hello world!</h1>

         <iframe src="https://www.youtube.com/embed/pfTTHx9kCHk" width="853" height="480" frameborder="0" allowfullscreen></iframe>
         <a href="{{url_for('success')}}">Return to main page</a>
         
          """
      else:
         print "weak"
         return """
         <h1>Hello world!</h1>

         <iframe src="https://www.youtube.com/embed/pfTTHx9kCHk" width="853" height="480" frameborder="0" allowfullscreen></iframe>
         <a href="{{url_for('success')}}">Return to main page</a>

          """
   
@app.route('/articlesmodified1',methods =['GET', 'POST'])      
def articlesmodified1():
   return render_template("articlesmodified1.html")
   

if __name__ == '__main__':
   app.run()
