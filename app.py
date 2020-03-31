import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'listOfPosts'
app.config["MONGO_URI"] = os.environ.get("Mongoinfo")
app.secret_key = os.environ.get("Secretkey")

mongo = PyMongo(app)
login_manager = LoginManager()


@app.route('/')
@app.route('/get_posts')
def get_posts():
    return render_template("posts.html", posts=mongo.db.adminPosts.find())


@app.route('/add_post')
def add_post():
    return render_template('addpost.html')


@app.route('/update_delete')
def update_delete():
    return render_template('updatedelete.html')


@app.route('/insert_post', methods=['POST'])
def insert_post():
    posts = mongo.db.adminPosts
    posts.insert_one(request.form.to_dict())
    return redirect(url_for('get_posts'))


@app.route('/edit_post/<post_id>')
def edit_post(post_id):
    the_post = mongo.db.adminPosts.find_one({"_id": ObjectId(post_id)})
    return render_template('editpost.html', post=the_post)

@app.route('/update_post/<post_id>', methods=["POST"])
def update_post(post_id):
    posts = mongo.db.adminPosts
    posts.update( {'_id': ObjectId(post_id)},
    {
        'title':request.form.get('title'),
        'dates':request.form.get('dates'),
        'article':request.form.get('article'),
        'author': request.form.get('author'),
    })
    return redirect(url_for('get_posts'))

@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    mongo.db.adminPosts.remove({'_id': ObjectId(post_id)})
    return redirect(url_for('get_posts'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
