#!/usr/bin/env python3
# coding:utf-8
import os
import sys

DEBUG = 0
HOST = "0.0.0.0"
PORT = 8000
DOMAIN = ".shucheng-ai.com"
PROJECT_LIMIT = 10  # 总project限额
PAGE_LIMIT = 10  # 每页限额

# path
_PATH = os.path.abspath(os.path.dirname(__file__))
SERVER_PATH = os.path.abspath(os.path.dirname(_PATH))
CLOUD_PATH = os.path.abspath(os.path.dirname(SERVER_PATH))

WWW_PATH = os.path.abspath(os.path.dirname(CLOUD_PATH))

STATIC_PATH = os.path.abspath(os.path.join(CLOUD_PATH, "wda_static"))
STATIC_DIST_PATH = os.path.abspath(os.path.join(STATIC_PATH, "dist"))

# wda-auth-decorators
AUTH_DECORATOR_PAHT = os.path.abspath(os.path.join(WWW_PATH, "wda-auth-decorators"))
# sys.path.append(AUTH_DECORATOR_PAHT)

# project database 172.17.0.1
DB_HOST = "172.17.0.1"
DB_PORT = 15433
DB_USERNAME = "admin"
DB_PASSWORD = "admin"

# auth database
AUTH_DB_HOST = "172.17.0.1"
AUTH_DB_PORT = 15432
AUTH_DB_USERNAME = "admin"
AUTH_DB_PASSWORD = "admin"

# wda auth
WDA_AUTH_URL = 'http://auth.shucheng-ai.com'
WDA_AUTH_LOGIN_URL = 'http://auth.shucheng-ai.com/auth/login'

# layout
LAYOUT_URL = 'http://layout.shucheng-ai.com'
LAYOUT_PROJECT_URL = 'http://layout.shucheng-ai.com/api/check_project?project_id='

# layout2
LAYOUT2_URL = 'http://layout2.shucheng-ai.com'
LAYOUT2_PROJECT_URL = 'http://layout2.shucheng-ai.com/api/auth/project/check?project_id='

# cad
CAD_URL = "http://cad.shucheng-ai.com"
CAD_PROJECT_URL = "http://cad.shucheng-ai.com/check_project?project_id="

# resource model
# http://resource-model.shucheng-ai.com/index?project_id=${}
RESOURCE_MODEL_URL = 'http://resource-model.shucheng-ai.com'
RESOURCE_MODEL_PROJECT_URL = 'http://resource-model.shucheng-ai.com/index?project_id='

PROJECT_PATH = "/project"
LAYOUT_PROJECT_PATH = "/project/layout_project"
RESOURCE_MODEL_PROJECT_PATH = "/project/resource_model_project"

# DATA ANALYTICS
DATA_ANALYTICS_PROJECT_URL = "http://analytics.shucheng-ai.com/index/defaultdata?project_id="

# help doc
DOC_FILES = [
    {
        "name": "Layout 说明文档",
        "path": "Layout_design-user_manual",
    },
    {
        "name": "Layout 产品手册",
        "path": "Layout_design-product_feature",
    }
]

try:
    from .local_config import *
except:
    pass

print('server path:', SERVER_PATH)
print('cloud path:', CLOUD_PATH)
print('www path:', WWW_PATH)
print('auth decorators path:', AUTH_DECORATOR_PAHT)
print('static dist path:', STATIC_DIST_PATH)
