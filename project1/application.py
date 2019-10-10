import os
# import requests
# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "WSPQYHxOwJq5n8j4TsQQA", "isbns": "9781632168146"})
# print(res.json())

from flask import Flask, render_template, session
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


@app.route("/")
def Login():
    return render_template("login.html")

@app.route("/register")
def Register():
    return render_template("register.html")

@app.route("/search")
def Search():
    return render_template("Search.html")