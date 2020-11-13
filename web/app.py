from flask import Flask, render_template
import requests
import itertools
from flask_bootstrap import Bootstrap
import os
# from get_recommendations import recommend
from flask import request

app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
    genres = ["Action","Comedy","Drama","Fantasy","Horror","Mystery","Romance","Thriller","Western"]
    return render_template('index.html', genres=genres)

@app.route('/match', methods=['POST'])
def match():
    user_order = request.json['user_order']
    return ' '.join(user_order)
    #return render_template('match.html', user_order=user_order)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
