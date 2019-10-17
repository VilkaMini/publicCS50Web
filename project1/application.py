import os
# import requests
# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "WSPQYHxOwJq5n8j4TsQQA", "isbns": "9781632168146"})
# print(res.json())

from flask import Flask, render_template, session, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=["GET", "POST"])
def Login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("search.html")

@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        engine.execute("INSERT INTO users (username, password) VALUES (:username, :password)", username=request.form.get("username"), password=request.form.get("password"))
        return render_template("login.html")

@app.route("/search", methods=["GET", "POST"])
def Search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        return render_template("bookpage.html")