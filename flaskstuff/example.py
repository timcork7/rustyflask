from flask import Flask, flash, redirect, render_template, request, session, abort
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sputnik7#"
)
app = Flask(__name__)

@app.route('/')
def hello_world():
    users = getData()
    return render_template('test.html', title='Welcome', members=users)

@app.route('/index')
def index():
   return '<b>Hello World</b>'


@app.route("/hello")
def hello():
     name = 'Rosalia'
     return render_template('layout.html', title='Welcome', username=name)

def getData():
    mycursor = mydb.cursor()
    mycursor.execute("select B1_PER_ID1,B1_PER_ID2,B1_PER_ID3 from tc_db.b1permit limit 20;")
    myresult = mycursor.fetchall()
    return myresult

if __name__ == '__main__':
   app.run()


