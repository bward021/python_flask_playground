from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from werkzeug.utils import redirect

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
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

@ app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()

        flash("Your book was added! :)", "success")

        return redirect('/books')
    else:
        return render_template('add-book.html')

@app.route('/books', methods=['GET'])
def get_books():
    all_books = Book.query.all()
        
    return render_template("books.html", books=all_books)

@app.route('/book/<id>', methods=['GET'])
def get_single_book(id):
    book = Book.query.get(id)
    print(id)
    print(book)
    return render_template('book.html', book = book)

@app.route('/delete-book/<id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash("Your book was deleted! :)", "danger")
    return redirect('/books')

@app.route('/edit-book/<id>', methods=['GET', 'POST'])
def edit_book(id):
    if request.method == "POST":
        book = Book.query.get(id)
        title = request.form.get('title')
        author = request.form.get('author')
        book.title = title
        book.author = author
        flash('Book was Edited :)', 'info')
        db.session.commit()
        return redirect('/books')
    else:
        book = Book.query.get(id)
        return render_template('edit-book.html', book=book)



@ app.route('/looping')
def looping():
    numbers = [1, 2, 3, 4, 5]
    return render_template('looping.html', data=numbers)

if __name__ == '__main__':
    app.run(debug=True)

