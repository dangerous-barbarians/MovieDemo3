SELECT username ,phone_number FROM users WHERE username = (SELECT username_friend FROM friends WHERE username_me ='张三');