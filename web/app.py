from flask import Flask, render_template
import requests
import itertools
from flask_bootstrap import Bootstrap
import os
# from get_recommendations import recommend
from flask import request

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def index():
    genres = ["Action","Comedy","Drama","Fantasy","Horror","Mystery","Romance","Thriller","Western"]
    return render_template('index.html', genres=genres)

@app.route('/match', methods=['GET','POST'])
def match():
    user_order = request.json['user_order']
    return render_template('match.html', user_order=user_order)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
