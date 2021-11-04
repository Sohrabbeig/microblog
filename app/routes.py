from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Amirhossein"}
    posts = [
        {
            "author": {"username": "Amirhossein"},
            "body": "Beautiful day in Edmonton!"
        },
        {
            "author": {"username": "Tahmineh"},
            "body": "It is cold!"
        }
    ]
    return render_template("index.html", title="Home",user=user, posts=posts)