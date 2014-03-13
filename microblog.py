from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import configs
import os
from datetime import datetime
from collections import deque
from flaskext.bcrypt import Bcrypt
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
mode = os.getenv('FLASK_MODE') or 'default'
app.config.from_object(configs[mode])
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    time = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, text):
        self.title = title
        self.test = text
        self.time = datetime.utcnow()

    def __repr__(self):
        return '<post %r>' % self.title


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pswd = db.Column(db.String(60))
    posts = db.relationship('post', backref='poster')

    def __init__(self, name, pswd):
        self.name = name
        self.pswd = bcrypt.generate_password_hash(pswd)


def write_post(title, text):
    newentry = Post(title, text)
    db.session.add(newentry)
    db.session.commit()
    return


def read_posts():
    # Post.query().order_by(Post.id.desc()).all()
    posts = deque()
    for i in Post.query.all():
        posts.appendleft(i)
    return posts


def read_post(num):
    return Post.query.get(num)


@app.route('/')
def list_view():
    posts = read_posts()
    page = render_template('list.html', posts=posts)
    return page


@app.route('/post/<int:id>')
def post_view(id):
    post = read_post(id)
    page = render_template('list.html', posts=post)
    return page


if __name__ == '__main__':
    manager.run()
