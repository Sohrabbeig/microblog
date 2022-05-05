from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Amirhossein'}
    posts = [
        {'author': {'username': 'Mikael'},
        'body': 'Nice weather!'},
        {'author': {'username': 'Esmael'},
        'body': "Let's go to the gym."}
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)