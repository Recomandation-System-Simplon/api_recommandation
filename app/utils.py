from os import pipe
import pandas as pd
from flask import current_app
import numpy as np


from app.db import db
import json

def format_data_books(data_housing: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD

    Args:
        data_housing (pd.DataFrame): dataframe provenant du fichier csv

    Returns:
        pd.DataFrame: Le dataframe converti
    """
    data_housing[
        [
            "population",
            "housing_median_age",
            "total_rooms",
            "total_bedrooms",
            "households",
            "median_house_value",
        ]
    ] = data_housing[
        [
            "population",
            "housing_median_age",
            "total_rooms",
            "total_bedrooms",
            "households",
            "median_house_value",
        ]
    ].astype(
        pd.Int64Dtype()
    )
    return data_housing


def books_results_to_dataframe(data_books: pd.DataFrame):
    """Transforme un dataframe provenant d'une requete sql en dataframe similaire à celui du fichier csv

    Args:
        data_books (pd.DataFrame): Le dataframe provenant de la requete sql

    Returns:
        pd.DataFrame: Un dataframe similaire au fichier csv
    """
    # On élimine les colonnes id et created_date du dataframe
    data_books.drop(columns=["ho_id", "ho_created_date", "ho_updated_date"], inplace=True)
    # On renomme les colonnes
    data_books = data_books.rename(
        columns={
            "ho_longitude": "longitude",
            "ho_latitude": "latitude",
            "ho_housing_median_age": "housing_median_age",
            "ho_total_rooms": "total_rooms",
            "ho_total_bedrooms": "total_bedrooms",
            "ho_population": "population",
            "ho_households": "households",
            "ho_median_income": "median_income",
            "ho_median_house_value": "median_house_value",
            "ho_ocean_proximity": "ocean_proximity",
        }
    )
    return data_books

