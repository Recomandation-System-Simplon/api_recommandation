from os import pipe
import pandas as pd
from flask import current_app
import numpy as np


from app.db import db
import json





def format_data_user(to_read_data, ratings_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        to_read_data,ratings_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    user = pd.concat([to_read_data.user_id, ratings_data.user_id])
    user = user.sort_values()
    user = user.drop_duplicates()
    user = user.to_frame()
    user = user.reset_index()
    user = user.drop(columns={"index"})
    user.user_id = user.user_id.astype("Int64")

    return user


def format_data_rates(ratings_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        ratings_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    rates = ratings_data.rating
    rates = rates.sort_values()
    rates = rates.drop_duplicates()
    rates = rates.to_frame()
    rates = rates.reset_index()
    rates = rates.drop(columns="index")
    rates = rates.reset_index()
    rates = rates.rename(columns={"index": "ratings_id"})
    rates.ratings_id = rates.ratings_id + 1

    colonne_int = ["ratings_id","rating"]

    for col in colonne_int:
        rates[col] = rates[col].astype("Int64")
    return rates
    


def format_data_books(book_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        book_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    liste_colonne_drop = [
        "work_id",
        "books_count",
        "isbn",
        "average_rating",
        "language_code",
        "image_url",
        "small_image_url",
        "ratings_count",
        "work_ratings_count",
        "work_text_reviews_count",
        "ratings_1",
        "ratings_2",
        "ratings_3",
        "ratings_4",
        "ratings_5",
    ]

    books = book_data

    for i in liste_colonne_drop:
        books = books.drop(columns=i)
    books = books.dropna()

    colonne_int = ["book_id","goodreads_book_id","isbn13","original_publication_year"]

    for col in colonne_int:
        books[col] = books[col].astype("Int64")

    books = books.dropna()
    books = books.rename(columns={"isbn13": "ISBN"})

    return books


def format_data_ratings(ratings_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        ratings_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    ratings = ratings_data.rename(columns={"rating": "rating_id"})
    
    colonne_int = ["user_id","book_id","rating_id"]

    for col in colonne_int:
        ratings[col] = ratings[col].astype("Int64")
    return ratings


def format_data_to_read(to_read_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        to_read_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    to_read = to_read_data
    to_read = to_read.reset_index()
    to_read = to_read.rename(columns={"index": "to_read_id"})
    to_read.to_read_id = to_read.to_read_id + 1

    colonne_int = ["to_read_id","user_id","book_id"]

    for col in colonne_int:
        to_read[col] = to_read[col].astype("Int64")

    return to_read


def format_data_tags(tags_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        tags (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    tags = tags_data
    tags.tag_id = tags.tag_id + 1
    tags.tag_id = tags.tag_id.astype("Int64")
    return tags


def format_data_goodread_book(book_data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        book_data (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    goodread_book = book_data
    goodread_book = goodread_book.goodreads_book_id
    goodread_book = goodread_book.sort_values()
    goodread_book = goodread_book.drop_duplicates()
    goodread_book = goodread_book.to_frame()
    goodread_book = goodread_book.reset_index()
    goodread_book = goodread_book.drop(columns={"index"})
    goodread_book.goodreads_book_id = goodread_book.goodreads_book_id.astype("Int64")
    return goodread_book




