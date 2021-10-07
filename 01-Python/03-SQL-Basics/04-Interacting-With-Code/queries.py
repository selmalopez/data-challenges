# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')


def directors_count(db):

    query1 = """
    SELECT
    count(*)
    FROM directors
    """
    db.execute(query1)
    results = db.fetchone()
    return results[0]

    # return the number of directors contained in the database
    # YOUR CODE HERE


def directors_list(db):

    query2 = """
    SELECT directors.name
    FROM directors
    ORDER BY directors.name
    """
    db.execute(query2)
    results = db.fetchall()
    return [i[0] for i in results]

    # return the list of all the directors sorted in alphabetical order
    # YOUR CODE HERE


def love_movies(db):

    query3 = """
    SELECT movies.title
    FROM movies
    WHERE (title LIKE "%love%")
    ORDER BY movies.title
    """
    db.execute(query3)
    results = db.fetchall()
    return [i[0] for i in results]

    # return the list of all movies which contain the word "love" in their title, sorted in alphabetical order
    # YOUR CODE HERE


def directors_named_like_count(db, name):

    query4 = f"""
    SELECT
    count (*)
    FROM directors
    WHERE directors.name LIKE ?

    """
    db.execute(query4,(f"%{name}%",))
    results = db.fetchone()
    return results[0]

    # return the number of directors which contain a given word in their name
    # YOUR CODE HERE


def movies_longer_than(db, min_length):

    query5 = """
    SELECT movies.title
    FROM movies
    WHERE movies.minutes >= ?
    ORDER by movies.title
    """
    db.execute(query5,(min_length,))
    results = db.fetchall()
    return [i[0] for i in results]

    # return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    # YOUR CODE HERE
