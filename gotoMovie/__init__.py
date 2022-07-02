import os
from flask import Flask, render_template
from . import database as db
from . import user, movie, houduan, others


def create_app(test_config=None):
    # create and configure the app
    application = Flask(__name__, instance_relative_config=True)
    application.config['JSON_AS_ASCII'] = False
    application.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(application.instance_path, '../instance/gotoMovie.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        application.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        application.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(application.instance_path)
    except OSError:
        pass

    db.init_app(application)
    application.register_blueprint(user.bp)
    application.register_blueprint(movie.bp)

    return application


application = create_app()


# 主页加载界面
@application.route('/')
def loading():
    return render_template("Blurry_Loading.html")


# 主页界面
@application.route('/index_page')
def index():
    return render_template("index.html")


# 登录界面
@application.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")


# 注册界面
@application.route('/register', methods=['POST', 'GET'])
def register():
    print('1')
    return render_template('register.html')


# 个人中心界面
@application.route('/home_page', methods=['POST', 'GET'])
def home_page():
    user_information = user.get_my_information()
    friend_list = others.get_friend_list()
    # user_coupon_list = get_user_coupon_list()
    # return render_template("home_page.html", user_information=user_information, yaoyue=user_coupon_list,
    #                        friend_list=friend_list)
    return render_template("home_page.html", user_information=user_information, yaoyue=houduan.yaoyue,
                           friend_list=friend_list)


# 电影详情界面
@application.route('/details_page', methods=['POST', 'GET'])
def details_page():
    title = '肖申克的救赎'
    stitle = '一切的一切都要从越狱说起'
    mingju = '"向往自由，向往生活"'
    release_date = '2020-7-8'
    brife = "小女孩千寻和父母一起在森林里迷了路，走过了一条神秘的隧道之后进入了一小镇。奇怪的是整个镇子一个人也没有。千寻的父母看到有一处店铺里存放着大量新"
    img = "../static/img/1.jpg"
    daoyan = "导演：宫崎骏"
    dic = {}
    dic[1] = title
    dic[2] = stitle
    dic[3] = mingju
    dic[4] = release_date
    dic[5] = brife
    dic[6] = img
    dic[7] = 999
    dic[8] = daoyan
    return render_template('details_page.html', data=dic)


# 用户邀约界面
@application.route('/invite_page')
def invite_page():
    return render_template("invite_page.html")


# 聊天界面
@application.route('/chat_room')
def chat_room():
    return render_template("chat_room.html")


@application.route('/fly', methods=['POST', 'GET'])
def fly():
    return render_template('fly.html')


"""
sqlite3.fetchone 也就是一行 用 dict 可以转换成字典
sqlite3.fetchall list类包装了sqlite.row   可以用 for in 解包 然后各个值封装成dict 然后整合成 list[dict]
"""
