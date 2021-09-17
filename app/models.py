from dataclasses import dataclass
from pandas.core.frame import DataFrame
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin
from app.db import db


@dataclass
class Books(db.Model, SerializerMixin):
    """Table books de la BDD, il est possible de faire des requete sql
    avec books.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "books"
    book_id = db.Column("book_id", db.Integer, primary_key=True)
    goodreads_book_id = db.db.Column("goodreads_book_id", db.Integer)
    best_book_id = db.Column("best_book_id", db.Integer)
    isbn = db.Column("isbn", db.Integer)
    authors = db.Column("authors", db.VARCHAR())
    original_publication_year = db.Column("original_publication_year", db.DECIMAL)
    original_title = db.Column("original_title", db.VARCHAR())
    title = db.Column("title", db.VARCHAR())
    ratings_count = db.Column("ratings_count", db.Integer)
    work_ratings_count = db.Column("work_ratings_count", db.Integer)
    work_text_reviews_count = db.Column("work_text_reviews_count", db.Integer)
    ratings_1 = db.Column("ratings_1", db.Integer)
    ratings_2 = db.Column("ratings_2", db.Integer)
    ratings_3 = db.Column("ratings_3", db.Integer)
    ratings_4 = db.Column("ratings_4", db.Integer)
    ratings_5 = db.Column("ratings_5", db.Integer)


@dataclass
class Ratings(db.Model, SerializerMixin):
    """Table ratings de la BDD, il est possible de faire des requete sql
    avec books.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "ratings"
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    book_id = db.db.Column("book_id", db.Integer, db.ForeingKey("books.book_id"))
    rating = db.Column("rating", db.Integer)


@dataclass
class To_read(db.Model, SerializerMixin):
    """Table to_read de la BDD, il est possible de faire des requete sql
    avec books.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "to_read"
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    book_id = db.db.Column("book_id", db.Integer,)




