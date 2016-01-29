# -*- coding: utf-8 -*-
from app.commands.common import *
from app.commands.hehe import *

COMMAND_WORDS = {
    'RPG': show_commands,
    '菜单': show_commands,
    '个人信息': show_info,
    '登录RPG': login,
    '退出RPG': logout,
    '计算': calc,
}
