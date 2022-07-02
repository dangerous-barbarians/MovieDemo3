from flask import Blueprint, request, g, session
from .database import connect_db

bp = Blueprint('others', __name__, url_prefix='/others')


# @bp.route('/friend-list', methods=['GET'])
# @login_required
# def get_friend_list():
#     """
#
#     :return: friend_list : type is list[ dict{}, ... ]
#     """
#     db = connect_db()
#     sql = "SELECT username as friend_name,phone_number as friend_phone_number " \
#           "FROM users WHERE username = (SELECT username_friend FROM friends WHERE username_me =?)"
#     friend_list_tmp = db.execute(sql, (g.user.username,)).fetchall()
#     friend_list = []
#     db.commit()
#     for i in range(len(friend_list_tmp)):
#         friend_list.append(dict(friend_list_tmp[i]))
#
#     return friend_list

@bp.route('/friend-list', methods=['GET'])
def get_friend_list():
    """

    :return: friend_list : type is list[ dict{}, ... ]
    """
    db = connect_db()
    sql = "SELECT username ,phone_number " \
          "FROM users WHERE username in (SELECT username_friend FROM friends WHERE username_me =?)"
    friend_list_tmp = db.execute(sql, (session.get('username'),)).fetchall()
    friend_list = []
    db.commit()
    for i in range(len(friend_list_tmp)):
        friend_list.append(dict(friend_list_tmp[i]))
        print(dict(friend_list_tmp[i]))

    return friend_list


@bp.route('/friend-information', methods=['POST'])
def get_friend_information():
    """

    :return: friend_information : type is dict{}
    """
    friend_name = request.form.get('friend_name')
    db = connect_db()
    sql = "SELECT username,head_portrait_address,gender,age,phone_number,self_introduction FROM users WHERE username =?"
    friend_information = db.execute(sql, (friend_name,)).fetchone()
    db.commit()
    friend_information = dict(friend_information)
    return friend_information


@bp.route('/delete-friend', methods=['POST'])
def delete_friend():
    friend_name = request.form.get('friend_name')
    db = connect_db()
    sql = "DELETE FROM friends WHERE username_me =? AND username_friend =?"
    db.execute(sql, (session.get('username'), friend_name))
    db.commit()
    information = "您删除了好友" + friend_name
    return information


@bp.route('/same-movie-users', methods=['GET'])
def get_same_movie_user_list():
    movie_name = session.get('movie_name')
    db = connect_db()
    sql = "SELECT username,head_portrait_address,self_introduction FROM users " \
          "WHERE username in (SELECT other_username FROM test_same_movie_users WHERE username=? AND movie_name=?)"

    movie_user_list_tmp = db.execute(sql, (session.get('username'), movie_name)).fetchall()
    movie_user_list = []
    db.commit()
    for i in range(len(movie_user_list_tmp)):
        movie_user_list.append(dict(movie_user_list_tmp[i]))

    return movie_user_list
