import os
from flask import Flask, render_template, redirect, request, url_for
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'listOfPosts'
app.config["MONGO_URI"] = os.environ.get("Mongoinfo")
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['emailaddress'],
    "MAIL_PASSWORD": os.environ['emailpassword']
}

app.config.update(mail_settings)
mail = Mail(app)

mongo = PyMongo(app)

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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
