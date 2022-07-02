from flask import Blueprint, request, session
from .database import connect_db

bp = Blueprint('movie', __name__, url_prefix='/movie')


@bp.route('/movie-list', methods=['POST'])
def get_movie_list():
    """

    :return: hot_movies : type is list[ dict{},...]
        upcoming_movies : type is list[ dict{},...]
    """
    hot_movies_tmp = get_hot_movie_list()
    upcoming_movies_tmp = get_upcoming_movie_list()
    hot_movies = []
    upcoming_movies = []
    for i in range(len(hot_movies_tmp)):
        hot_movies.append(dict(hot_movies_tmp[i]))
    for i in range(len(upcoming_movies_tmp)):
        upcoming_movies.append(dict(upcoming_movies_tmp[i]))
    
    movies = {"hot_movies": hot_movies, "upcoming_movies": upcoming_movies}
    return movies


@bp.route('/information', methods=['POST'])
def get_movie_information():
    """

    :return: movie_information : type is dict{}
    """
    movie_name = request.form.get('movie_name')
    session['movie_name'] = movie_name
    db = connect_db()
    sql = "SELECT * FROM movies WHERE movie_name = ?"
    movie_information = db.execute(sql, (movie_name,)).fetchone()
    db.commit()
    movie_information = dict(movie_information)
    return movie_information


@bp.route("/characters_information", methods=['POST'])
def get_characters_information():
    """

    :return:characters_information : type is list[ dict{},...]
    """
    movie_name = request.form.get('movie_name')
    db = connect_db()
    sql = "SELECT character_name,picture_address,synopsis FROM characters WHERE movie_name = ?"
    characters_information_tmp = db.execute(sql, (movie_name,)).fetchall()
    db.commit()
    characters_information = []
    for i in range(len(characters_information_tmp)):
        characters_information.append(dict(characters_information_tmp[i]))

    return characters_information


@bp.route("/director_information", methods=['POST'])
def get_director_information():
    """

    :return:characters_information : type is dict{...}
    """
    movie_name = request.form.get('movie_name')
    db = connect_db()
    sql = "SELECT character_name,picture_address,synopsis FROM characters WHERE movie_name = ?"
    characters_information = db.execute(sql, (movie_name,)).fetchone()
    db.commit()
    characters_information = dict(characters_information)

    return characters_information


def get_hot_movie_list():
    db = connect_db()
    sql = "SELECT movie_name, movie_picture_address, movie_state FROM movies WHERE movie_state =?"
    movie_state = 'hot'
    hot_movies = db.execute(sql, (movie_state,)).fetchall()
    db.commit()

    return hot_movies


def get_upcoming_movie_list():
    db = connect_db()
    sql = "SELECT movie_name, movie_picture_address, movie_state FROM movies WHERE movie_state=?"
    movie_state = 'upcoming'
    upcoming_movies = db.excute(sql, (movie_state,)).fetchall()
    db.commit()

    return upcoming_movies
