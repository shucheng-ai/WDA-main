#!/usr/bin/env python3
# coding:utf-8
import os

mode = 0  # product
_PATH = os.path.abspath(os.path.dirname(__file__))

try:
    conf = os.path.abspath(os.path.join(_PATH, "static.conf"))
    with open(conf, "r") as f:
        text = f.read().replace(" ", "").replace("\n", "")
        if text.find("dev") != -1:
            mode = 1
except:
    pass

if mode == 0:
    print("read static dist")
else:
    # npm run server
    path = os.path.abspath(os.path.join(_PATH, "wda"))
    command = "cd {} ; ls ;npm run serve".format(path)
    print("run npm server")
    print(command)
    os.system(command)
