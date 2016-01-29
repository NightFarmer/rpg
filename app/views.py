# -*- coding: utf-8 -*-
from app import app, db
from app.commands import *
from app.models import User, Role
import json
from flask import request


@app.route('/')
def index():
    return "hello world, flask"


@app.route('/hello', methods=["Post"])
def hello():
    param = request.stream.read().decode("gbk")
    print(param)
    param_dict = json.JSONDecoder().decode(param);
    from_qq = param_dict['fromQQ']
    msg = param_dict['msg']
    global command
    is_command = False
    for command in COMMAND_WORDS.keys():
        if msg.startswith(command):
            is_command = True
            break
    if is_command:
        msg = msg.replace(command, "", 1)
        command_func = COMMAND_WORDS.get(command)
        return command_func(msg, from_qq).encode('gbk')
    return ""


@app.route('/init/')
def init():
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_zhangsan = User(username='zhangsan', role=admin_role)
    user_zhangsan.qq = "846401807"
    user_lisi = User(username='lisi', role=user_role)
    user_lisi.qq = "100"
    db.session.add_all([admin_role, mod_role, user_role, user_zhangsan, user_lisi])
    db.session.commit()
    return "init"


@app.route("/find/")
def find():
    user_list = User.query.all()
    print(user_list)
    return str(len(user_list))
