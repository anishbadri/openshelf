from datetime import datetime
from app import db

class Celebrity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    reads = db.relationship('Book', secondary='celebrity_reads', backref='celebrity', lazy='dynamic')

    def __repr__(self):
        return f'{self.name}'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200))
    imageLink =  db.Column(db.String(400))
    googleid = db.Column(db.String(20), unique=True)
    # author = db.Column(db.String(120), unique=True, nullable=False)
    isbn = db.Column(db.String(13))
    authors = db.relationship('Author', secondary='author_book', backref='books')

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

AuthorBook = db.Table('author_book',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

CelebrityReads = db.Table('celebrity_reads',
    db.Column('celebrity_id', db.Integer, db.ForeignKey('celebrity.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)