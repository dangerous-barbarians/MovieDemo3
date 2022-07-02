INSERT INTO users(head_portrait_address, username, password, gender, age, phone_number, address, self_introduction)
VALUES ('/static/img/1.jpg', '张三', '123zhangsan', '男', 18, '18062630855', '华中师范大学南湖校区', '我是一个大傻逼'),
       ('/static/img/1.jpg', 'lisi', '123lisi', '男', 20, '182637889', '华中师范大学南湖校区', '我是一个lisi'),
       ('/static/img/1.jpg', 'wangwu', '123wangwu', '男', 17, '18062632376', '华中师范大学南湖校区', '我是一个wangwu');

INSERT INTO test_same_movie_users(movie_name, username, other_username)
VALUES ('test_movie1', 'lyj', 'fly'),
       ('test_movie1', 'lyj', 'tbb'),
       ('test_movie1', 'lyj', 'ly'),
       ('test_movie1', 'lyj', 'ymt');

INSERT INTO friends(username_me, username_friend, make_friend_time)
VALUES ('李毅佳', 'zhangsan', '2020-11-1'),
       ('李毅佳', 'lisi', '2019-7-12'),
       ('李毅佳', 'wangwu', '2021-5-23');

INSERT INTO movies(movie_name, movie_state, movie_score, time_length, release_date, drop_date, movie_picture_address,
                   synopsis)
VALUES ('人生大事', 'upcoming', 7.4, 112, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2874262709.jpg', 'none'),
       ('你是我的春天', 'upcoming', 0, 122, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2874262709.jpg', 'none'),
       ('珠峰队长', 'upcoming', 0, 83, '2020-11-2', '2020-12-2',
        'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2874784921.jpg', 'none'),
       ('焚情', 'upcoming', 0, 87, '2020-11-2', '2020-12-2',
        'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2874213575.jpg', 'none'),
       ('神奇动物：邓布利多之谜', 'upcoming', 5.9, 142, '2020-11-2', '2020-12-2',
        'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2871106106.jpg', 'none'),
       ('侏罗纪世界3', 'upcoming', 6.3, 147, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2873135507.jpg', 'none'),
       ('精灵旅社4：变身大冒险', 'upcoming', 6.3, 88, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2870571717.jpg', 'none'),
       ('地瓜味的冰激凌', 'upcoming', 0, 94, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2874841049.jpg', 'none'),
       ('暗恋·橘生淮南', 'upcoming', 4.6, 0, '2020-11-2', '2020-12-2',
        'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2873970594.jpg', 'none'),
       ('唐顿庄园2', 'upcoming', 8.2, 120, '2020-11-2', '2020-12-2',
        'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2871809800.jpg', 'none'),
       ('一周的朋友', 'upcoming', 4.8, 106, '2020-11-2', '2020-12-2',
        'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2874367740.jpg', 'none'),
       ('边缘行者', 'upcoming', 5, 113, '2020-11-2', '2020-12-2',
        'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2871147122.jpg', 'none'),
       ('哆啦A梦：大雄的宇宙小战争', 'upcoming', 6.2, 108, '2020-11-2', '2020-12-2',
        'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2873563629.jpg', 'none'),
       ('镜世界', 'upcoming', 0, 85, '2020-11-2', '2020-12-2',
        'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2873276186.jpg', 'none'),
       ('迷途重生', 'upcoming', 0, 87, '2020-11-2', '2020-12-2',
        'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2874794696.jpg', 'none');

INSERT INTO characters(character_name, movie_name, picture_address, synopsis)
VALUES ('朱一龙', '人生大事', 'none', 'none'),
       ('杨恩又', '人生大事', 'none', 'none'),
       ('王戈', '人生大事', 'none', 'none'),
       ('周冬雨', '你是我的春天', 'none', 'none'),
       ('尹昉', '你是我的春天', 'none', 'none'),
       ('宋小宝', '你是我的春天', 'none', 'none'),
       ('苏拉王平', '珠峰队长', 'none', 'none'),
       ('泽勇', '珠峰队长', 'none', 'none'),
       ('崔舟萍', '珠峰队长', 'none', 'none'),
       ('郑嘉颖', '焚情', 'none', 'none'),
       ('陈静', '焚情', 'none', 'none'),
       ('朱晨丽', '焚情', 'none', 'none'),
       ('埃迪·雷德梅恩', '神奇动物：邓布利多之谜', 'none', 'none'),
       ('裘德·洛', '神奇动物：邓布利多之谜', 'none', 'none'),
       ('麦斯·米科尔森', '神奇动物：邓布利多之谜', 'none', 'none'),
       ('克里斯·帕拉特', '侏罗纪世界3', 'none', 'none'),
       ('布莱丝·达拉斯·霍华德', '侏罗纪世界3', 'none', 'none'),
       ('劳拉·邓恩', '侏罗纪世界3', 'none', 'none'),
       ('布赖恩·哈尔', '精灵旅社4：变身大冒险', 'none', 'none'),
       ('安迪·萨姆伯格', '精灵旅社4：变身大冒险', 'none', 'none'),
       ('赛琳娜·戈麦斯', '精灵旅社4：变身大冒险', 'none', 'none'),
       ('张艺瀚', '地瓜味的冰激凌', 'none', 'none'),
       ('王啸坤', '地瓜味的冰激凌', 'none', 'none'),
       ('张雪迎', '暗恋·橘生淮南', 'none', 'none'),
       ('辛云来', '暗恋·橘生淮南', 'none', 'none'),
       ('伍嘉成', '暗恋·橘生淮南', 'none', 'none'),
       ('米歇尔·道克瑞', '唐顿庄园2', 'none', 'none'),
       ('休·博纳维尔', '唐顿庄园2', 'none', 'none'),
       ('伊丽莎白·麦戈文', '唐顿庄园2', 'none', 'none'),
       ('赵今麦', '一周的朋友', 'none', 'none'),
       ('林一', '一周的朋友', 'none', 'none'),
       ('沈月', '一周的朋友', 'none', 'none'),
       ('任贤齐', '边缘行者', 'none', 'none'),
       ('任达华', '边缘行者', 'none', 'none'),
       ('方中信', '边缘行者', 'none', 'none'),
       ('水田山葵', '哆啦A梦：大雄的宇宙小战争', 'none', 'none'),
       ('大原惠美', '哆啦A梦：大雄的宇宙小战争', 'none', 'none'),
       ('嘉数由美', '哆啦A梦：大雄的宇宙小战争', 'none', 'none'),
       ('罗翔', '镜世界', 'none', 'none'),
       ('冯萌梦', '迷途重生', 'none', 'none'),
       ('王一漪', '迷途重生', 'none', 'none'),
       ('于歌', '迷途重生', 'none', 'none');

INSERT INTO directors(director_name, movie_name, picture_address, synopsis)
VALUES ('刘江江', '', '人生大事', 'none'),
       ('周楠', '', '你是我的春天', 'none'),
       ('吴曦', '', '珠峰队长', 'none'),
       ('刘伟恒', '', '焚情', 'none'),
       ('大卫·叶茨', '', '神奇动物：邓布利多之谜', 'none'),
       ('科林·特莱沃若', '', '侏罗纪世界3', 'none'),
       ('德里克·德莱蒙', '', '精灵旅社4：变身大冒险', 'none'),
       ('王翀', '', '地瓜味的冰激凌', 'none'),
       ('黄斌', '', '暗恋·橘生淮南', 'none'),
       ('西蒙·柯蒂斯', '', '唐顿庄园2', 'none'),
       ('林孝谦', '', '一周的朋友', 'none'),
       ('黄明升', '', '边缘行者', 'none'),
       ('山口晋', '', '哆啦A梦：大雄的宇宙小战争', 'none'),
       ('袁杰', '', '镜世界', 'none'),
       ('赵晖', '', '迷途重生', 'none');



INSERT INTO user_coupons(username_inviter, username_invitee, coupon_name, coupon_state, release_date, expiration_date)
VALUES ('lyj', 'fly', 'test_movie18元二人优惠券', 'valid', '2020-11-15', '2020-11-21');

INSERT INTO coupons(coupon_type, money_save, lasting_dates, deadline)
VALUES ('test_movie_coupon', 18, 7, '2020-11-30');





