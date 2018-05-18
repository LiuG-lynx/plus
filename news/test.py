#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/poet_news'
db = SQLAlchemy(app)

class Category(db.Model):
    # 'primary_key=True' include auto_increment...
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Category %r>' % self.name
    def save(self):
        db.session.add(self)
        db.session.commit()

class File(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('Category.id'))
    category = db.relationship('Category', backref=db.backref('file_course' ,lazy = 'dynamic'))
    content = db.Column(db.Text)
    
    def __init__(self, title, created_time,category_id,content):
        self.title = title
        self.created_time = created_time
        self.category_id = category_id
        self.content = content
    def __repr__(self):
        return '<File %r>' % self.title
    def save(self):
        db.session.add(self)
        db.session.commit()

# Create tables
db.create_all()
java = Category('Java')
python = Category('python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is Cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
files = File.query.all()
print(files)
categories = Category.query.all()
print(categories)
