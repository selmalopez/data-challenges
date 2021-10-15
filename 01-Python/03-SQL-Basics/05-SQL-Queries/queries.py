# pylint: disable=C0103, missing-docstring
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''

    query = """
    SELECT movies.genres, movies.title, directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    """
    db.execute(query)
    results = db.fetchall()
    return results


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query = """"
    SELECT movies.title
    FROM movies
    WHERE movies.start_year > directors.death_year
    JOIN movies ON movies.directors_id = movies.id
    """
    db.execute(query)
    results = late_released_movies(db)
    return results


    # YOUR CODE HERE
def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    results = stats_on(db,genre_name)
    return results
    # YOUR CODE HERE


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    # YOUR CODE HERE

    results = top_five_directors_for(db, genre_name)
    return results


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    results = movie_duration_buckets(db)
    return results
    # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    results = top_five_youngest_newly_directors(db)
    return results
    # YOUR CODE HERE
