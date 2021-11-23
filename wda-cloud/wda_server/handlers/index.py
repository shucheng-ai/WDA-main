#!/usr/bin/env python3
# coding:utf-8
from .base import BaseHandler
from config import WDA_AUTH_URL, WDA_AUTH_LOGIN_URL, LAYOUT_URL, LAYOUT_PROJECT_URL, RESOURCE_MODEL_URL, \
    RESOURCE_MODEL_PROJECT_URL, LAYOUT2_PROJECT_URL


class ConfigHandler(BaseHandler):

    def _get(self, **kwargs):
        data = {
            "status": 1,
            "data": {
                "login_url": WDA_AUTH_LOGIN_URL,
                "demo": {
                    "layout": f"{LAYOUT_PROJECT_URL}1",
                    "resource_model": f"{RESOURCE_MODEL_PROJECT_URL}1",
                },
                "layout_project_url": LAYOUT_PROJECT_URL,
                "layout2_project_url": LAYOUT2_PROJECT_URL,
                "resource_model_project_url": RESOURCE_MODEL_PROJECT_URL,
            }
        }
        return data
