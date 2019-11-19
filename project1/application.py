import csv
import urllib.request
import os
import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "WSPQYHxOwJq5n8j4TsQQA", "isbns": "9781632168146"})
print(res.json())

from flask import Flask, render_template, session, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from functools import wraps

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


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/", methods=["GET", "POST"])
def Login():
    session.clear()
    if request.method == "GET":
        return render_template("login.html")
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        userchecking = engine.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        result = userchecking.fetchall()
        if len(result):
            session["user_id"] = result[0][0]
            return render_template("search.html")
        else:
            return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def Register():
    session.clear()
    if request.method == "GET":
        return render_template("register.html")
    else:
        username=request.form.get("username")
        password=request.form.get("password")
        usercheck = engine.execute(f"SELECT * FROM users WHERE username='{username}'")
        result = usercheck.fetchall()
        if not len(result):
            engine.execute(f"INSERT INTO users (username, password) VALUES('{username}', '{password}')")
            return render_template("login.html")
        else:
            return render_template("register.html")


@app.route("/logout", methods=["GET", "POST"])
def Logout():
    session.clear()
    return render_template("login.html")

@app.route("/search", methods=["GET", "POST"])
@login_required
def Search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        book=request.form.get("search")
        books = engine.execute(f"SELECT * FROM books WHERE isbn LIKE '%%{book}%%' OR title LIKE '%%{book}%%' OR author LIKE '%%{book}%%'")
        result = books.fetchall()
        return render_template("books.html", sbooks=result)

@app.route("/book", methods=["GET", "POST"])
@login_required
def Book():
    if request.method == "GET":
        return render_template("search.html")
    else:
        info = request.form.get("result")
        print("Forma", info)
        return render_template("bookpage.html", bookinfo=info)