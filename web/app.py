from flask import Flask, render_template
import requests
import itertools
from flask_bootstrap import Bootstrap
import os
from countInversions import countInversions
from flask import request
from flask_pymongo import PyMongo
from flask import jsonify
import json
from bson import json_util


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["MONGO_URI"] = "mongodb://paa:21milEmmEa57yKDx@paa-shard-00-00.se53e.mongodb.net:27017,paa-shard-00-01.se53e.mongodb.net:27017,paa-shard-00-02.se53e.mongodb.net:27017/movie_recommendation?ssl=true&replicaSet=atlas-10i7up-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo = PyMongo(app)

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

genres = ["Action","Comedy","Drama","Fantasy","Horror","Mystery","Romance","Thriller","Western"]

@app.route('/')
def index():
    return render_template('index.html', genres=genres)

@app.route('/record_user_preference', methods=['POST'])
def record_user_preference():
    user_order = list(request.json['user_order'])
    if not user_order:
        user_order = genres  
    user_name = request.json['user_name']  
    user_preference = mongo.db.users.insert_one({'name':user_name, "preference":user_order})
    return jsonify(success=True), 200 


@app.route('/get_best_matches', methods=['POST'])
def get_best_matches():
    user_order = list(request.json['user_order'])
    if not user_order:
        user_order = genres  
    user_name = request.json['user_name']  

    users = mongo.db.users.find({},{ "_id": 0})
    
    results = []
    n =  len(user_order)
    max_inversions =  n*(n-1)/2

    for user in users:
        current_user_name = user["name"]
        if current_user_name != user_name: 
            current_choice = user["preference"]
            ordered = [user_order.index(choice)+1 for choice in current_choice]
            inversions = countInversions(ordered)[1]
            score = int(100-((inversions/max_inversions)*100))
            results.append({"name":current_user_name,"score":score})        

    return render_template('match.html', results=results)


@app.route('/match', methods=['GET','POST'])
def match():
    user_order = list(request.json['user_order'])
    if not user_order:
        user_order = genres
    return render_template('match.html', user_order=user_order)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
