from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from countInversions import countInversions
from flask import request
from flask_pymongo import PyMongo
from flask import jsonify
from operator import itemgetter


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["MONGO_URI"] = "mongodb://paa:21milEmmEa57yKDx@paa-shard-00-00.se53e.mongodb.net:27017,paa-shard-00-01.se53e.mongodb.net:27017,paa-shard-00-02.se53e.mongodb.net:27017/movie_recommendation?ssl=true&replicaSet=atlas-10i7up-shard-0&authSource=admin&retryWrites=true&w=majority"
mongo = PyMongo(app)


genres = [
    "Action",
    "Comedy",
    "Drama",
    "Fantasy",
    "Horror",
    "Mystery",
    "Romance",
    "Thriller",
    "Western"]


@app.route('/')
def index():
    return render_template('index.html', genres=genres)


@app.route('/record_user_preference', methods=['POST'])
def record_user_preference():
    '''
    Inserts a user and his/her respective preferences of movie genres
    '''
    user_order = list(request.json['user_order'])
    if not user_order:
        user_order = genres
    user_name = request.json['user_name']
    user_contact = request.json['user_contact']
    mongo.db.users.insert_one(
        {'name': user_name, "preference": user_order, 'contact': user_contact})
    return jsonify(success=True), 200


@app.route('/get_best_matches', methods=['POST'])
def get_best_matches():
    '''

    '''
    user_order = list(request.json['user_order'])
    if not user_order:
        user_order = genres
    user_name = request.json['user_name']

    users = mongo.db.users.find({}, {"_id": 0})

    results = []
    n = len(user_order)
    max_inversions = n * (n - 1) / 2

    for user in users:
        current_user_name = user["name"]
        if current_user_name != user_name:
            current_user_contact = user["contact"]
            current_choice = user["preference"]
            ordered = [
                user_order.index(choice) +
                1 for choice in current_choice]
            inversions = countInversions(ordered)[1]
            score = int(100 - ((inversions / max_inversions) * 100))
            results.append({"name": current_user_name,
                            "score": score, "contact": current_user_contact})

    results = sorted(results, key=itemgetter('score'), reverse=True)[:5]
    return render_template('best_matches.html', results=results)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
