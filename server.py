from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt        
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=[a-zA-Z0-9!@#$%^&*()_+=-]{8,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).*$')    
app = Flask(__name__)
app.secret_key = "keep it secret"
bcrypt = Bcrypt(app) #
database = "placeholder"

@app.route("/")
def index():
    return render_template("test.html")

if __name__== "__main__":
    app.run(debug=True)   
