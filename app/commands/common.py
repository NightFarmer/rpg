# -*- coding: utf-8 -*-
from app.services import *


def show_commands(msg, qq):
    return """操作指令：
登录RPG
个人信息
退出RPG"""


def login(msg, qq):
    login_service()
    return reply_qq(qq) + "成功登录RPG！"


def show_info(msg, qq):
    return reply_qq(qq) + "个人信息：啥也没有~"


def logout(msg, qq):
    return reply_qq(qq) + "成功退出RPG！"


def reply_qq(qq):
    return '[CQ:at,qq=' + qq + '] '
