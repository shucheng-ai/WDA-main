#!/usr/bin/env python3
# coding:utf-8
from wda_decorators.wda import WDA as WDA_AUTH
from config import AUTH_DB_HOST, AUTH_DB_PORT, AUTH_DB_USERNAME, AUTH_DB_PASSWORD

wdaauth = WDA_AUTH(
    db_host=AUTH_DB_HOST,
    db_port=AUTH_DB_PORT,
    db_username=AUTH_DB_USERNAME,
    db_password=AUTH_DB_PASSWORD,
)
