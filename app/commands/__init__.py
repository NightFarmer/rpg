# -*- coding: utf-8 -*-
from app.commands.common import *
from app.commands.hehe import *

COMMAND_WORDS = {
    '查看': show_info,
    '登录': login,
    '退出': logout,
    '计算': calc,
}
