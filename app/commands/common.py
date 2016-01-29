# -*- coding: utf-8 -*-
from app.services import *


def login(msg, qq):
    login_service()
    return qq + "login" + msg


def show_info(msg, qq):
    return qq + "show_info" + msg


def logout(msg, qq):
    return qq + "logout" + msg


def reply_qq(qq):
    return '[CQ:at,qq=' + str(qq) + '] '
