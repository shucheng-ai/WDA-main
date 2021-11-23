#!/usr/bin/env python3
# coding:utf-8
from flask import request
from wda_decorators.db import init_engine
from wda_decorators.models import Session, User, UserInfo
from wda_decorators.utils import decode_session_data


class WDA(object):
    db_host = "127.0.0.1"
    db_port = 5432
    db_name = "shucheng"
    db_username = "admin"
    db_password = "admin"
    db_user_db = "auth_user"
    db_session_db = "django_session"
    db_group_db = "auth_group"
    db_permission_db = "auth_permission"
    db_engine = None

    def __init__(self,
                 db_host="127.0.0.1",
                 db_port=5432,
                 db_username="admin",
                 db_password="admin",
                 ):
        self.db_host = db_host
        self.db_port = db_port
        self.db_username = db_username
        self.db_password = db_password
        self.init_db()

    def init_db(self):
        engine = init_engine(
            host=self.db_host,
            port=self.db_port,
            username=self.db_username,
            password=self.db_password,
            dbname=self.db_name,
        )
        self.db_engine = engine

    def wda_auth(self, func):
        def wda_wrapper(*args, **kwargs):
            user = {
                "name": "",
                "uid": -1,
                "sessionid": ""
            }
            sessionid = request.cookies.get('sessionid')
            # sessionid = "test"
            session = Session.get_session(sessionid, self.db_engine)
            if session:
                data = decode_session_data(session.session_data)
                user["uid"] = int(data["_auth_user_id"])
                _user = User(user["uid"], self.db_engine)
                _userinfo = UserInfo(user["uid"], self.db_engine)
                user["name"] = _user.username
                user["sessionid"] = sessionid
                user["is_expired"] = 0
                if _userinfo.json():
                    user["has_info"] = True
                    user["info"] = _userinfo.json()
                    user["is_expired"] = _userinfo.is_expired()
                else:
                    user["has_info"] = False
                    user["info"] = {}
            kwargs["wda_user"] = user
            return func(*args, **kwargs)

        wda_wrapper.__name__ = func.__name__
        return wda_wrapper

    def wda_login_required(self, func):
        def wda_wrapper(*args, **kwargs):
            wda_user = kwargs.get("wda_user", {})
            if wda_user.get("uid") <= 0:
                kwargs["wda_is_login"] = False
            else:
                kwargs["wda_is_login"] = True
            return func(*args, **kwargs)

        wda_wrapper.__name__ = func.__name__
        return wda_wrapper

    def wda_permission_required(self, permission=''):
        def wda_decorator(func):
            def wda_wrapper(*args, **kwargs):
                kwargs["wda_require_permissions"] = permission
                kwargs["wda_has_permissions"] = False

                wda_user = kwargs.get("wda_user", None)
                if wda_user:
                    # test data
                    wda_user["company"] = ""

                    _user = User(wda_user["uid"], self.db_engine)
                    _permissions = _user.get_permissions(self.db_engine)
                    kwargs["wda_user_permissions"] = _permissions
                    if _permissions.get(permission):
                        kwargs["wda_has_permissions"] = True

                return func(*args, **kwargs)

            wda_wrapper.__name__ = func.__name__
            return wda_wrapper

        return wda_decorator

    def wda_group_required(self, group=""):
        def wda_decorator(func):
            def wda_wrapper(*args, **kwargs):
                kwargs["wda_in_group"] = False
                wda_user = kwargs.get("wda_user", None)
                if wda_user:
                    _user = User(wda_user["uid"], self.db_engine)
                    _groups = _user.get_groups(self.db_engine)
                    kwargs["wda_user_groups"] = _groups
                    if _groups.get(group):
                        kwargs["wda_in_group"] = True
                return func(*args, **kwargs)

            wda_wrapper.__name__ = func.__name__
            return wda_wrapper

        return wda_decorator
