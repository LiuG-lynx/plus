from flask import Flask, render_template
import os,os.path
import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String,DateTime,create_engine
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/poet_news'
db = SQLAlchemy(app)
engine = create_engine('mysql://root@localhost/poet_news')
app.config.update(dict(
    index_title = engine.execute('select title from file').fetchall(),
    news1 = engine.execute('select content,created_time,name from file,category where file.category_id=category.id and file.id=1').fetchall(),
    news2 = engine.execute('select content,created_time,name from file,category where file.category_id=category.id and file.id=2').fetchall()

))

class File(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('file-category', lazy='dynamic'))
    content = db.Column(db.Text)
    created_time = db.Column(db.DateTime)
    
    def __init__(self, title,created_time,category, content):
        self.title = title
        self.created_time = created_time
        self.content = content
        self.category = category
    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

@app.route('/')
def index():
    """ route method parameters only can pass through from rout
    """
    title_list = app.config['index_title']
    title_list1 = title_list[0]
    title_list2 = title_list[1]
    return render_template('index.html',title_world1=title_list1,title_world2=title_list2)


@app.route('/files/<file_id>')
def file(file_id):
    # like this
    if int(file_id) == 1:
        return render_template('file.html',file_name_content=app.config['news1'])
    elif int(file_id) == 2: 
        return render_template('file.html',file_name_content=app.config['news2'])
    else:
        return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

 

if __name__ == '__main__':
    
    try:
        db.create_all()
        java = Category('Java')
        py = Category( 'python')
        file1 = File('Hello Java',datetime.utcnow(),java,'File Content - Java is cool!')
        file2 = File('Hello Python',datetime.utcnow(),py,'File Content - Python is cool!')
        db.session.add(java)
        db.session.add(py)
        db.session.add(file1)
        db.session.add(file2)
        db.session.commit()
        files = File.query.all()
        categories = Category.query.all()
    except:   
        exit()
    finally:
        
        app.run()
        
