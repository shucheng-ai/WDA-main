#!/usr/bin/env python3
# coding:utf-8
import sys
import os

sys.path.append("..")

from wda_server.app.app import app
from wda_server.config import DEBUG, HOST, PORT
from wda_server.wsgi_server import run_wsgi
from wda_server.config import SERVER_PATH

print(sys.path)

mode = 0  # product

try:
    conf = os.path.abspath(os.path.join(SERVER_PATH, "server.conf"))
    with open(conf, "r") as f:
        text = f.read().replace(" ", "").replace("\n", "")
        if text.find("dev") != -1:
            mode = 1
except:
    pass

if mode == 0:
    print("run server(product mode:gevent wsgi server)")
    run_wsgi(app, HOST, PORT)
else:
    print("run server(dev mode:base flask server)")
    app.run(
        debug=True,
        host=HOST,
        port=PORT
    )
