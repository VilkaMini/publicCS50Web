import csv
import urllib.request
import os
import requests
import json
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
        usercheck = False
        info = request.form.get("result")
        goodreads = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "WSPQYHxOwJq5n8j4TsQQA", "isbns": f"{info}"})
        result = engine.execute(f"SELECT * FROM books WHERE isbn ='{info}'")
        review = engine.execute(f"SELECT * FROM reviews WHERE isbn ='{info}'")
        goodjson = goodreads.json()
        ratingcount = goodjson["books"][0]["ratings_count"]
        average = goodjson["books"][0]["average_rating"]
        review = review.fetchall()
        result = result.fetchall()
        if review != []:
            a=0
            for dic in review:
                if session["user_id"] == int(dic[4]):
                    usercheck = True
                a +=1
        return render_template("bookpage.html", bookinfo=result, reviews=review, userid=usercheck, average=average, count=ratingcount)

@app.route("/review", methods=["GET", "POST"])
@login_required
def Review():
    if request.method == "GET":
        return render_template("search.html")
    else:
        userid = session["user_id"]
        isbn = request.form.get("isbn")
        review = request.form.get("review")
        rating = request.form.get("rating")
        engine.execute(f"INSERT INTO reviews (isbn, review, rating, userid) VALUES ('{isbn}', '{review}', '{rating}', '{userid}')")
        return render_template("search.html")

@app.route("/api/<isbn>", methods=["GET"])
def Api(isbn):
    goodreads = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "WSPQYHxOwJq5n8j4TsQQA", "isbns": f"{isbn}"})
    bookInfo = engine.execute(f"SELECT * FROM books WHERE isbn ='{isbn}'")
    bookInfo = bookInfo.fetchall()
    goodreads = goodreads.json()
    print(goodreads)
    jDic = {"title": bookInfo[0][1],
            "author": bookInfo[0][2],
            "year": bookInfo[0][3],
            "isbn": bookInfo[0][0],
            "review_court": goodreads["books"][0]["ratings_count"],
            "average_score": goodreads["books"][0]["average_rating"]}
    return json.dumps(jDic)