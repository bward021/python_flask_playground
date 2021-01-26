from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(144), unique=False, nullable=False)
    author = db.Column(db.String(144), unique=False, nullable=False)

class BookSchema(ma.Schema):
    class Meta:
        fields = ('title', 'author', 'id')

bookSchema = BookSchema
booksSchema = BookSchema(many=True)


@ app.route('/')
def hello_world():
    return render_template('index.html')

@ app.route('/add-book')
def add_book():
    return render_template('add-book.html')

@ app.route('/looping')
def looping():
    numbers = [1, 2, 3, 4, 5]
    return render_template('looping.html', data=numbers)

if __name__ == '__main__':
    app.run(debug=True)

