#!/usr/bin/env python3
# coding:utf-8
from gevent.pywsgi import WSGIServer


def run_wsgi(app, host, port):
    print("run server(gevent wsgi)")
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()
