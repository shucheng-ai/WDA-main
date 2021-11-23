#!/usr/bin/env python3
# coding:utf-8
from flask import Flask
from flask.views import MethodView
from wda_decorators.wda import WDA
from wda_decorators.models import Session
import json

wda = WDA(
    db_host="172.17.0.1",
    db_port=15432,
    db_username="admin",
    db_password="admin",
)
res = Session.is_table_exists(wda.db_engine)
print(f"connect postgresql, session db: {res}")

app = Flask(
    __name__,
)


@app.route('/')
def index():
    return "hello flask"


@app.route('/auth')
@wda.wda_auth
def auth_handler(**kwargs):
    data = json.dumps(kwargs)
    return data


@app.route('/test')
@wda.wda_auth
@wda.wda_login_required
@wda.wda_group_required()
@wda.wda_permission_required()
def test_handler(**kwargs):
    data = {}
    data["user"] = kwargs.get("wda_user")
    data["groups"] = kwargs.get("wda_user_groups")
    data["permissions"] = kwargs.get("wda_user_permissions")
    return data


class PermissionHandler(MethodView):

    @wda.wda_auth
    @wda.wda_permission_required(permission="layout")
    def get(self, **kwargs):
        return json.dumps(kwargs)


class LoginHandler(MethodView):

    @wda.wda_auth
    @wda.wda_login_required
    def get(self, **kwargs):
        return json.dumps(kwargs)


class GroupHandler(MethodView):

    @wda.wda_auth
    @wda.wda_group_required()
    def get(self, **kwargs):
        return json.dumps(kwargs)


app.add_url_rule("/login", view_func=LoginHandler.as_view("login"))
app.add_url_rule("/group", view_func=GroupHandler.as_view("group"))
app.add_url_rule("/permission", view_func=PermissionHandler.as_view("permission"))

app.run(
    debug=True,
    host='0.0.0.0',
    port=5000
)
