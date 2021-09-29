import joblib
import numpy as np
import pandas as pd
from app.db import db


class PopularityModel:

    data = pd.read_sql_query(
        'SELECT books.book_id,books.goodreads_book_id,books.title,books.authors, count(rates.ratings) as "ratings_count", AVG(rates.ratings) as "average_rating" FROM books JOIN ratings ON (books.book_id = ratings.book_id) JOIN rates ON (rates.ratings_id = ratings.ratings_id) GROUP BY books.book_id ORDER BY "average_rating" DESC ,"ratings_count"',
        db.engine,
    )
    # Calcul de C, à partir des moyennes de notes
    C = data["average_rating"].mean()
    # Calcul de m, à partire du 50ème quantile
    m = data["ratings_count"].quantile(0.75)
    popularity_books= data[data["ratings_count"]>=m]
    
    # Fonction qui calcule la note pondérée
    def weighted_rating(x, m=m, C=C):

        v = x["ratings_count"]
        R = x["average_rating"]

        return ( v/(v+m) *R)+(m/(v+m)*C)

    popularity_books["weighted_rating"] = popularity_books.apply(weighted_rating, axis=1)

    
