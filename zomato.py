from flask import *
from flask_sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + BASE_DIR + '/test1.db'
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)


# Model
class Restaurant(db.Model):
	__tablename__ = 'restaurant'
	# Defining the fields
	id = db.Column(db.String(10), primary_key=TRUE)
	name = db.Column(db.String(100))
	city = db.Column(db.String(20))




@app.route("/zomato", methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('zomato.html')
    else:
        redirect ("/zomato/sign_up")
@app.route("/zomato/sign_up", methods = [ 'GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        return render_template( 'signup.html' )
@app.route("/zomato/log_in", methods = [ 'GET', 'POST' ])
def log_in():
    if request.method == 'POST':
        return render_template( 'login.html' )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True )
