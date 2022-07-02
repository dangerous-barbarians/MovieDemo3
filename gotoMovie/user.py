from flask import Blueprint, request, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from .database import connect_db


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    gender = request.form.get('gender')
    address = request.form.get('address')
    self_introduction = request.form.get('self_introduction')
    phone_number = request.form.get('phone_number')

    error = '无'
    db = connect_db()
    if not username:
        error = '用户名不能为空'
    elif not password:
        error = '密码不能为空'

    if error is None:
        try:
            sql = "INSERT INTO users(username,password,gender,phone_number,address,self_introduction) VALUES(?,?,?,?,?)"
            db.execute(sql, (username, generate_password_hash(password), gender, phone_number, address, self_introduction))
            db.commit()
        except db.IntegrityError:
            error = f"用户名： {username} 已经存在，请换一个用户名"

    if error is None:
        return
    else:
        return error


@bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    error = '无'
    db = connect_db()
    sql = "SELECT username,password FROM users WHERE username =? "
    user = db.execute(sql, (username,)).fetchone()
    db.commit()

    if user is None:
        error = '登陆失败，用户名或密码错误，或没有注册'
    elif not check_password_hash(user['password'], password):
        error = '密码错误，请重新尝试'

    if error == '无':
        session.clear()
        session['username'] = user['username']
        session['password'] = user['password']

    return error


# @bp.before_app_request
# def load_logged_in_user():
#     username = session.get('username')
#     if username is None:
#         g.user = None
#     else:
#         db = connect_db()
#         sql = "SELECT username,password FROM users WHERE username =?"
#         g.user = db.execute(sql, (username,)).fetchone()
#         db.commit()


# def login_required(view_function):
#     """
#     this is a decorator
#     """
#
#     @functools.wraps(view_function)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('user.login'))
#         return view_function(**kwargs)
#
#     return wrapped_view


@bp.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')


@bp.route('/information', methods=['GET'])
def get_my_information():
    """
    get user information
    only user self can see
    username,password,head_picture,gender,age,phone_number,self_introduction
    """

    db = connect_db()
    sql = "SELECT username,password,head_portrait_address,gender,age,phone_number,self_introduction,address" \
          " FROM users WHERE username =?"
    user_information = db.execute(sql, (session.get('username'),)).fetchone()
    db.commit()
    user_information = dict(user_information)
    return user_information


@bp.route('/edit-information', methods=['POST'])
def edit_information():
    username = session.get('username')
    head_portrait_new = request.form.get('head_portrait')
    gender_new = request.form.get('gender')
    age_new = request.form.get('age')
    phone_number_new = request.form.get('phone_number')
    self_introduction_new = request.form.get('self_introduction')
    address_new = request.form.get('address')
    db = connect_db()
    sql = None
    if head_portrait_new:
        sql = "UPDATE users SET head_portrait = ? WHERE username = ?"
        db.execute(sql, (head_portrait_new, username))
    if gender_new:
        if gender_new == '男' or gender_new == '女':
            sql = "UPDATE users SET gender = ? WHERE username = ?"
            db.execute(sql, (gender_new, username))
    if age_new:
        if 0 < age_new < 150:
            sql = "UPDATE users SET age = ? WHERE username = ?"
            db.execute(sql, (age_new, username))
    if phone_number_new:
        sql = "UPDATE users SET phone_number = ? WHERE username = ?"
        db.execute(sql, (phone_number_new, username))
    if self_introduction_new:
        sql = "UPDATE users SET self_introduction = ? WHERE username = ?"
        db.execute(sql, (self_introduction_new, username))
    if address_new:
        sql = "UPDATE users SET address = ? WHERE username = ?"
        db.execute(sql, (address_new, username))

    information = ""
    if sql:
        db.commit()
        information = "您成功修改个人信息"
    else:
        information = "您没能成功修改个人信息"
    return information


@bp.route('/edit-password', methods=['POST'])
def edit_password():
    password_new = request.form.get('password_new')
    password_old = request.form.get('password_old')
    db = connect_db()
    error = "您成功修改了密码"
    if password_old and password_new:
        if check_password_hash(session.get('password'), password_old):
            sql = "UPDATE users SET password = ? WHERE username = ?"
            db.execute(sql, (generate_password_hash(password_new), session.get('username')))
            db.commit()
            error += ("修改后的新密码是: " + password_new)
        else:
            error = "原密码错误，请重新尝试"
    else:
        error = "密码不允许为空，请重新尝试"

    return error










