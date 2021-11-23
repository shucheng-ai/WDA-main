#!/usr/bin/env python3
# coding:utf-8
from flask import Flask
from .urls import url_list, set_url
from .utils import mkdir
from config import STATIC_DIST_PATH, PROJECT_PATH, LAYOUT_PROJECT_PATH, RESOURCE_MODEL_PROJECT_PATH

mkdir(PROJECT_PATH)
mkdir(LAYOUT_PROJECT_PATH)
mkdir(RESOURCE_MODEL_PROJECT_PATH)

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder=STATIC_DIST_PATH,
    template_folder=STATIC_DIST_PATH
)

set_url(app, url_list)


@app.route('/')
@app.route('/my')
@app.route('/info')
@app.route('/index')
@app.route('/help')
@app.route('/pdf')
def index():
    return app.send_static_file('index.html')
