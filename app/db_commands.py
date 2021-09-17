import pandas as pd
from flask.cli import with_appcontext
from consolemenu import SelectionMenu
from flask import current_app
import numpy as np
#from app.models import ModelParams
from app.utils import format_data_books #, house_results_to_dataframe, regression
from app.db import db
from app.models import Books
import json


@click.command("insert-db")
@with_appcontext
def insert_db():
    """Insère les données nécessaire à l'utilisation de l'application"""
    # On récupère les données du fichier CSV dans un dataframe
    data_books = pd.read_csv("books.csv")
    # On format les données (int64 pour les champs) afin de les préparer à l'insertion
    data_books = format_data_books(data_books)
    # On insère les données dans la table House
    Books.insert_from_pd(data_books)
    print("Données dans la BDD insérées")
    
    
    # On confirme tous les changements pour la transaction
    db.session.commit()
    print("Tout a été inséré dans la base de données !")

    