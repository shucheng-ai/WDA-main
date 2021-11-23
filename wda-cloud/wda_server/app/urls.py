#!/usr/bin/env python3
# coding:utf-8
from handlers.project import ProjectHandler
from handlers.auth import AuthHandler, LougoutHandler
from handlers.index import ConfigHandler
from handlers.file import PdfHandler
from handlers.help import HelpHandler

from handlers.test import TestHandler


def set_url(app, url_list):
    count = 0
    for item in url_list:
        count += 1
        try:
            name = "router-{}-{}".format(item[0].replace('/', ''), count)
            app.add_url_rule(item[0], view_func=item[1].as_view(name))
        except Exception as e:
            print(e)


url_list = [
    ['/api/config', ConfigHandler],

    ['/api/auth', AuthHandler],
    ['/api/logout', LougoutHandler],

    ['/api/project', ProjectHandler],

    ['/api/test', TestHandler],

    ['/api/pdf', PdfHandler],
    ['/api/help', HelpHandler],
]
