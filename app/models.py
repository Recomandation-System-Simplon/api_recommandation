from dataclasses import dataclass
from pandas.core.frame import DataFrame
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin
from app.db import db


@dataclass
class User(db.Model, SerializerMixin):
    """Table user de la BDD, il est possible de faire des requete sql
    avec user.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "user"
    user_id = db.Column("user_id", db.Integer, primary_key=True)

    def insert_user_from_pd(user: DataFrame):
        user.to_sql("user", if_exists="append", con=db.engine, index=False)


@dataclass
class Rates(db.Model, SerializerMixin):
    """Table rates de la BDD, il est possible de faire des requete sql
    avec rates.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "rates"
    ratings_id = db.Column("ratings_id", db.Integer, primary_key=True)
    rating = db.Column("rating", db.Integer)

    def insert_rates_from_pd(rates: DataFrame):
        rates.to_sql("rates", if_exists="append", con=db.engine, index=False)


@dataclass
class Books(db.Model, SerializerMixin):
    """Table books de la BDD, il est possible de faire des requete sql
    avec books.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "books"
    book_id = db.Column("book_id", db.Integer, primary_key=True)
    goodreads_book_id = db.Column("goodreads_book_id", db.Integer, db.ForeignKey("goodread_book.goodreads_book_id"))
    best_book_id = db.Column("best_book_id", db.Integer)
    isbn = db.Column("isbn", db.Integer)
    authors = db.Column("authors", db.VARCHAR())
    original_publication_year = db.Column("original_publication_year", db.DECIMAL)
    original_title = db.Column("original_title", db.VARCHAR())
    title = db.Column("title", db.VARCHAR())

    def insert_books_from_pd(books: DataFrame):
        books.to_sql("rates", if_exists="append", con=db.engine, index=False)


@dataclass
class Ratings(db.Model, SerializerMixin):
    """Table ratings de la BDD, il est possible de faire des requete sql
    avec ratings.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "ratings"
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"),primary_key=True)
    book_id = db.Column("book_id", db.Integer, db.ForeignKey("books.book_id"),primary_key=True)
    rating_id = db.Column("ratings_id", db.Integer, db.ForeignKey("rates.ratings_id"),primary_key=True)

    def insert_ratings_from_pd(ratings: DataFrame):
        ratings.to_sql("ratings", if_exists="append", con=db.engine, index=False)


@dataclass
class To_read(db.Model, SerializerMixin):
    """Table to_read de la BDD, il est possible de faire des requete sql
    avec to_read.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "to_read"
    to_read_id = db.Column("to_read_id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"))
    book_id = db.Column("book_id", db.Integer, db.ForeignKey("books.book_id"))

    def insert_to_read_from_pd(to_read: DataFrame):
        to_read.to_sql("to_read", if_exists="append", con=db.engine, index=False)


@dataclass
class Tags(db.Model, SerializerMixin):
    """Table tags de la BDD, il est possible de faire des requete sql
    avec tags.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "tags"
    tags_id = db.Column("tag_id", db.Integer, primary_key=True)
    tag_name = db.Column("tag_name", db.VARCHAR())

    def insert_tags_from_pd(tags: DataFrame):
        tags.to_sql("tags", if_exists="append", con=db.engine, index=False)


@dataclass
class Goodread_book(db.Model, SerializerMixin):
    """Table goodread_book de la BDD, il est possible de faire des requete sql
    avec goodread_book.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "goodread_book"
    goodread_book_id = db.Column("goodread_book_id", db.Integer, primary_key=True)

    def insert_goodread_book_from_pd(goodread_book: DataFrame):
        goodread_book.to_sql(
            "goodread_book", if_exists="append", con=db.engine, index=False
        )


@dataclass
class Book_tags(db.Model, SerializerMixin):
    """Table book_tags de la BDD, il est possible de faire des requete sql
    avec book_tags.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "book_tags"
    goodread_book_id = db.Column(
        "goodread_book_id", db.Integer, db.ForeignKey("goodread_book.goodread_book_id"), primary_key=True
    )
    tags_id = db.Column("tag_id", db.Integer, db.ForeignKey("tags.tags_id"), primary_key=True)

    def insert_book_tag_from_pd(book_tags: DataFrame):
        book_tags.to_sql("book_tags", if_exists="append", con=db.engine, index=False)
