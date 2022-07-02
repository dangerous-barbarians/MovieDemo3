DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS friends;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS user_coupons;
DROP TABLE IF EXISTS coupons;
DROP TABLE IF EXISTS test_same_movie_users;


CREATE TABLE test_same_movie_users(
    movie_name TEXT NOT NULL,
    username TEXT NOT NULL,
    other_username TEXT NOT NULL,
    FOREIGN KEY(username,other_username) REFERENCES users(username,username)
);


CREATE TABLE users(
    head_portrait_address TEXT NOT NULL DEFAULT 'none',
    username TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL,
    gender TEXT NOT NULL DEFAULT '男',
    age INTEGER DEFAULT 20,
    self_introduction TEXT DEFAULT 'none',
    phone_number TEXT DEFAULT 'none',
    current_address TEXT DEFAULT 'none',
    address TEXT DEFAULT 'none'
);

CREATE TABLE friends(
    username_me TEXT NOT NULL,
    username_friend TEXT NOT NULL,
    make_friend_time  NOT NULL,
    FOREIGN KEY(username_me,username_friend) REFERENCES users(username,username)
);

CREATE TABLE movies(
    movie_name TEXT PRIMARY KEY UNIQUE NOT NULL,
    movie_state TEXT NOT NULL DEFAULT 'hot movie',
    movie_picture_address TEXT NOT NULL DEFAULT 'none',
    movie_score FLOAT NOT NULL DEFAULT 0,
    time_length INTEGER NOT NULL DEFAULT 0,
    release_date TEXT NOT NULL DEFAULT 'none',
    drop_date TEXT NOT NULL DEFAULT 'none',
    synopsis TEXT NOT NULL DEFAULT 'none'
);

CREATE TABLE directors(
    director_name TEXT NOT NULL,
    movie_name TEXT NOT NULL,
    picture_address TEXT NOT NULL DEFAULT 'none',
    synopsis TEXT NOT NULL DEFAULT 'none',
    PRIMARY KEY(director_name,movie_name),
    FOREIGN KEY(movie_name) REFERENCES movies(movie_name)
);

CREATE TABLE characters(
    character_name TEXT NOT NULL,
    movie_name TEXT NOT NULL,
    picture_address TEXT NOT NULL DEFAULT 'none',
    synopsis TEXT NOT NULL DEFAULT 'none',
    PRIMARY KEY(character_name,movie_name),
    FOREIGN KEY(movie_name) REFERENCES movies(movie_name)
);

CREATE TABLE user_coupons(
    username_inviter TEXT NOT NULL,
    username_invitee TEXT NOT NULL,
    coupon_name TEXT NOT NULL,
    coupon_state TEXT NOT NULL DEFAULT 'valid',
    release_date TEXT NOT NULL DEFAULT 'none',
    expiration_date TEXT NOT NULL DEFAULT 'none',
    PRIMARY KEY(username_inviter,username_invitee,coupon_name),
    FOREIGN KEY(username_inviter,username_invitee) REFERENCES users(username,username)
);

CREATE TABLE coupons(
    coupon_type TEXT PRIMARY KEY UNIQUE NOT NULL,
    money_save INTEGER NOT NULL,
    lasting_dates INTEGER NOT NULL,
    deadline TEXT NOT NULL
);

