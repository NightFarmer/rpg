# -*- coding: utf-8 -*-
from app.commands.common import reply_qq


def calc(msg, qq):
    result = ""
    try:
        msg = msg.strip("")
        msg = msg.strip()
        msg = msg.replace("&amp;", "&")
        result = eval(msg)
    except:
        result = "计算公式错误"
    return reply_qq(qq) + """

原式：
%s

结果：
%s
""" % (msg, result)
