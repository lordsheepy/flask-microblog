from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import configs
import os
from datetime import datetime
from collections import deque

app = Flask(__name__)
mode = os.getenv('FLASK_MODE') or 'default'
app.config.from_object(configs[mode])
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    time = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.test = text
        self.time = datetime.now()

    def __repr__(self):
        return '<post %r>' % self.title


def write_post(title, text):
    newentry = Post(title, text)
    db.session.add(newentry)
    db.session.commit()
    return


def read_posts():
    posts = deque()
    for i in Post.query.all():
        posts.appendleft(i)
    return posts


def read_post(num):
    return Post.query.get(num)
