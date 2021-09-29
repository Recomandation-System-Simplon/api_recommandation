import joblib
import numpy as np
import pandas as pd
import pyarrow.feather as feather
from scipy.sparse.linalg import svds
from scipy.linalg import sqrtm
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from app.db import db


def TrainPopularityBasedModel():

    data = pd.read_sql_query(
        'SELECT books.book_id,books.goodreads_book_id,books.title,books.authors, count(rates.ratings) as "ratings_count", AVG(rates.ratings) as "average_rating" FROM books JOIN ratings ON (books.book_id = ratings.book_id) JOIN rates ON (rates.ratings_id = ratings.ratings_id) GROUP BY books.book_id ORDER BY "average_rating" DESC ,"ratings_count"',
        db.engine,
    )
    # Calcul de C, à partir des moyennes de notes
    C = data["average_rating"].mean()
    # Calcul de m, à partire du 50ème quantile
    m = data["ratings_count"].quantile(0.50)
    # On ne garde que les livres au dessus de m
    popularity_books = data[data["ratings_count"] >= m].copy()

    # Calcul du weighted_rating de chaque livre
    v = popularity_books["ratings_count"]
    R = popularity_books["average_rating"]

    popularity_books["weighted_rating"] = (v / (v + m) * R) + (m / (v + m) * C)
    popularity_books = popularity_books.sort_values("weighted_rating", ascending=False)

    return feather.write_feather(
        popularity_books[["book_id", "goodreads_book_id", "title", "weighted_rating"]],
        "data/popularity_books",
    )


def TrainCollaborativeFiltering():

    request = pd.read_sql_query("SELECT * FROM ratings", db.engine)
    # Création de la table user // book avec les notes déjà données
    R_df = request.pivot(
        index="user_id", columns="book_id", values="ratings_id"
    ).fillna(0)

    # on récupère seulement les valeurs pour le svds
    R = R_df.values
    # Calcul la moyenne des notes mise par chaque user, pour la retirer (on la rajoutera à la fin)
    user_ratings_mean = np.mean(R, axis=1)
    user_ratings_mean = np.float16(user_ratings_mean)
    R_demeaned = R - user_ratings_mean.reshape(-1, 1)

    latent_dimension = 90  # Après une étude sur cette valeur (de 90 à 110) et sur l'erreur myenne et écart type prediction - note réelle, on a décidé de prendre 90 (rapport erreur/temps de calcul)

    U, sigma, Vt = svds(R_demeaned, k=latent_dimension)

    sigma = np.diag(sigma)
    s_root = sqrtm(sigma)

    Usk = np.dot(U, s_root)
    Usk = np.float16(Usk)  # Passage float64 à float16

    skV = np.dot(s_root, Vt)
    skV = np.float16(skV)  # Passage float64 à float16

    predicted_rating = np.dot(
        Usk, skV
    )  # Calcul des notes de chaque user pour chaque livre

    predicted_rating = predicted_rating + user_ratings_mean.reshape(
        -1, 1
    )  # On rajoute la moyenne

    preds_df = pd.DataFrame(predicted_rating, columns=R_df.columns, index=R_df.index)

    # Exporter les prédictions pour les usitliser dans Recommandation.py
    feather.write_feather(preds_df, "data/predicted_ratings")



def TrainContentBased():

    tags = pd.read_sql_query("SELECT * FROM tags",db.engine)
    book_tags = pd.read_sql_query("SELECT * FROM book_tags",db.engine)
    books = pd.read_sql_query("SELECT * FROM books",db.engine)

    def get_tag_id(x):

        tag_id = pd.read_sql_query("SELECT tag_id FROM tags WHERE tag_name = %s" %(str(x)),db.engine)['tag_id'].item()
