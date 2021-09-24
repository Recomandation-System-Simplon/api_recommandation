from collections import UserString
import click
import pandas as pd
from flask.cli import with_appcontext
#from getpass import getpass
#from werkzeug.security import generate_password_hash
#from consolemenu import SelectionMenu

from app.db import db
from app.utils import (
    format_data_user,
    format_data_books,
    format_data_ratings,
    format_data_tags,
    format_data_to_read,
    format_data_goodread_book,
    format_data_rates,
    format_data_book_tag)




from app.models import (
    User,
    Rates,
    Tags,
    Books,
    Goodread_book,
    Book_tags,
    Ratings,
    To_read)
    



@click.command("insert-db")
@with_appcontext
def insert_db():
    """Insère les données nécessaire à l'utilisation de l'application"""
    # On récupère les données des fichiers CSV dans des dataframe
    # data_housing = pd.read_csv("housing.csv")
    book_data = pd.read_csv("data/books.csv")
    ratings_data = pd.read_csv("data/ratings.csv")
    tags_data = pd.read_csv("data/tags.csv")
    to_read_data = pd.read_csv("data/to_read.csv")
    book_tags_data = pd.read_csv("data/book_tags.csv")

    # On format les données (int64 pour les champs) afin de les préparer à l'insertion
    # data_housing = format_data_housing(data_housing)
    
    user = format_data_user(to_read_data, ratings_data)
    rates = format_data_rates(ratings_data)
    books = format_data_books(book_data)
    ratings = format_data_ratings(ratings_data)
    to_read = format_data_to_read(to_read_data)
    tags = format_data_tags(tags_data)
    goodread_book = format_data_goodread_book(book_data)
    book_tags = format_data_book_tag(book_tags_data)

    # On insère les données dans la table House
    User.insert_user_from_pd(user)
    Rates.insert_rates_from_pd(rates)
    Tags.insert_tags_from_pd(tags)
    Goodread_book.insert_goodread_book_from_pd(goodread_book)
    Book_tags.insert_book_tag_from_pd(book_tags) 
    Books.insert_books_from_pd(books)
    To_read.insert_to_read_from_pd(to_read)
    Ratings.insert_ratings_from_pd(ratings)
    

    # House.insert_from_pd(data_housing)
    print("Données dans la BDD insérées")


    # On confirme tous les changements pour la transaction
    db.session.commit()
    print("Tout a été inséré dans la base de données !")
