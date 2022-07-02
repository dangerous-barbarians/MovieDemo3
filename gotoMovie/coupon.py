import datetime
from flask import Blueprint, request, g, session
from .database import connect_db
import random

bp = Blueprint('coupon', __name__, url_prefix='/coupon')


@bp.route('/coupon-list', methods=['POST'])
def get_user_coupon_list():
    """

    :return: user_coupon_list : type is list[ dict{},...]
    """
    """
        first condition: me : username as inviter
        second condition: me : username as invitee
    """

    db = connect_db()
    sql = "SELECT * FROM user_coupons WHERE username_inviter = ?"
    inviter_coupon_list_tmp = db.execute(sql, (session.get('username'),)).fetchall()
    sql = "SELECT * FROM user_coupons WHERE username_invitee = ?"
    invitee_coupon_list_tmp = db.execute(sql, (session.get('username'),)).fetchall()
    user_coupon_list = []
    db.commit()
    for i in range(len(inviter_coupon_list_tmp)):
        user_coupon_list.append(dict(inviter_coupon_list_tmp[i]))

    for i in range(len(invitee_coupon_list_tmp)):
        user_coupon_list.append(dict(invitee_coupon_list_tmp[i]))

    return user_coupon_list


@bp.route('/coupon-information', methods=['POST'])
def get_user_coupon():
    """
    :return: user_coupon_list : type is dict{}
    """
    username_inviter = request.form.get('username_inviter')
    username_invitee = request.form.get('username_invitee')
    coupon_name = request.form.get('coupon_name')
    db = connect_db()
    sql = "SELECT * FROM user_coupons WHERE username_inviter = ? AND username_invitee= ? AND coupon_name = ?"
    user_coupon_tmp = db.execute(sql, (username_inviter, username_invitee, coupon_name)).fetchone()
    db.commit()
    user_coupon_information = dict(user_coupon_tmp)
    return user_coupon_information


@bp.route('/generate-display-coupon', methods=['POST'])
def generate_display_user_coupon():
    movie_name = session.get('movie_name')
    username_inviter = request.form.get('username_inviter')
    username_invitee = request.form.get('username_invitee')

    db = connect_db()
    sql = " SELECT money_save, lasting_dates FROM coupons"
    result_list = db.execute(sql).fetchall()
    length = len(result_list)
    result = result_list[random.randint(1, length)]

    money_save = result['money_save']
    lasting_dates = result['lasting_dates']
    coupon_state = "valid"
    release_date = datetime.date.today()
    expiration_date = release_date + datetime.timedelta(days=lasting_dates)
    coupon_name = movie_name + money_save + "元二人优惠券"

    sql = "INSERT INTO user_coupons(username_inviter,username_invitee, coupon_name, coupon_state, release_date, expiration_date)" \
          "VALUES(?,?,?,?,?,?)"
    db.execute(sql, (username_inviter, username_invitee, coupon_name, coupon_state, release_date, expiration_date))
    db.commit()

    coupon_information = {'username_inviter': username_inviter, 'username_invitee': username_invitee,
                          'coupon_name': coupon_name, 'coupon_state': coupon_state, 'release_date': release_date,
                          'expiration_date': expiration_date}
    return coupon_information
