from pandas import DataFrame
from app.db import db
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, DECIMAL, BIGINT
from sqlalchemy.orm import relationship




class User(db.Model):
    """Table user de la BDD, il est possible de faire des requete sql
    avec user.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "user"
    user_id = Column("user_id", Integer, primary_key=True)


    def insert_user_from_pd(user: DataFrame):
        user.to_sql("user", if_exists="append", con=db.engine, index=False)


class Rates(db.Model):
    """Table rates de la BDD, il est possible de faire des requete sql
    avec rates.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "rates"
    ratings_id = Column("ratings_id", Integer, primary_key=True)
    rating = Column("ratings", Integer)



    def insert_rates_from_pd(rates: DataFrame):
        rates.to_sql("rates", if_exists="append", con=db.engine, index=False)


class Books(db.Model):
    """Table books de la BDD, il est possible de faire des requete sql
    avec books.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "books"
    book_id = Column("book_id", Integer, primary_key=True)
    goodreads_book_id = Column(
        "goodreads_book_id", Integer, ForeignKey("goodreads_book.goodreads_book_id")
    )
    best_book_id = Column("best_book_id", Integer)
    isbn = Column("isbn", BIGINT)
    authors = Column("authors", VARCHAR)
    original_publication_year = Column("original_publication_year", DECIMAL)
    original_title = Column("original_title", VARCHAR)
    title = Column("title", VARCHAR)



    def insert_books_from_pd(books: DataFrame):
        books.to_sql("books", if_exists="append", con=db.engine, index=False)


class Ratings(db.Model):
    """Table ratings de la BDD, il est possible de faire des requete sql
    avec ratings.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "ratings"
    id = Column("id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("user.user_id"))
    book_id = Column("book_id", Integer, ForeignKey("books.book_id"))
    rating_id = Column("ratings_id", Integer, ForeignKey("rates.ratings_id"))

    def insert_ratings_from_pd(ratings: DataFrame):
        ratings.to_sql("ratings", if_exists="append", con=db.engine, index=False)

class To_read(db.Model):
    """Table to_read de la BDD, il est possible de faire des requete sql
    avec to_read.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "to_read"
    to_read_id = Column("to_read_id", Integer, primary_key=True)
    user_id = Column("user_id", Integer, ForeignKey("user.user_id"))
    book_id = Column("book_id", Integer, ForeignKey("books.book_id"))

    def insert_to_read_from_pd(to_read: DataFrame):
        to_read.to_sql("to_read", if_exists="append", con=db.engine, index=False)



class Tags(db.Model):
    """Table tags de la BDD, il est possible de faire des requete sql
    avec tags.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "tags"
    tags_id = Column("tag_id", Integer, primary_key=True)
    tag_name = Column("tag_name", VARCHAR)

    book_tag = relationship("Book_tags")
    def insert_tags_from_pd(tags: DataFrame):
        tags.to_sql("tags", if_exists="append", con=db.engine, index=False)


class Goodread_book(db.Model):
    """Table goodread_book de la BDD, il est possible de faire des requete sql
    avec goodread_book.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "goodreads_book"
    goodreads_book_id = Column("goodreads_book_id", Integer, primary_key=True)

    def insert_goodread_book_from_pd(goodread_book: DataFrame):
        goodread_book.to_sql(
            "goodreads_book", if_exists="append", con=db.engine, index=False
        )


class Book_tags(db.Model):
    """Table book_tags de la BDD, il est possible de faire des requete sql
    avec book_tags.query (voir la doc de flask-sqlalchemy)
    """

    __tablename__ = "book_tags"
    id = Column("id", Integer, primary_key=True)
    goodreads_book_id = Column(
        "goodreads_book_id", Integer, ForeignKey("goodreads_book.goodreads_book_id")
    )
    tags_id = Column("tag_id", Integer, ForeignKey("tags.tag_id"))

    def insert_book_tag_from_pd(book_tags: DataFrame):
        book_tags.to_sql("book_tags", if_exists="append", con=db.engine, index=False)
