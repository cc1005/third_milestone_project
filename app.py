import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'listOfPosts'
app.config["MONGO_URI"] = os.environ.get("Mongoinfo")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_posts')
def get_posts():
    return render_template("posts.html", posts=mongo.db.adminPosts.find())

@app.route('/add_post')
def add_post():
    return render_template('addpost.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
