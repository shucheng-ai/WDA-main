#!/usr/bin/env python3
# coding:utf-8
from .base import BaseHandler
from app.auth import wdaauth
from flask.views import MethodView
from flask import make_response, request
from config import DOMAIN

import json


class AuthHandler(BaseHandler):

    @wdaauth.wda_auth
    @wdaauth.wda_group_required()
    def _get(self, **kwargs):
        data = {
            "status": 1
        }
        data["user"] = kwargs.get("wda_user")
        data["groups"] = kwargs.get("wda_user_groups")

        if data["user"]["uid"] <= 0:
            data["is_login"] = False
        else:
            data["is_login"] = True

        return data


class LougoutHandler(MethodView):

    def get(self, **kwargs):
        res = json.dumps({"status": 1})
        resp = make_response(res)
        resp.set_cookie('sessionid', '', expires=0, domain=DOMAIN)

        return resp
