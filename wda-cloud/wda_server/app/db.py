#!/usr/bin/env python3
# coding:utf-8
from wda_model.wda_model.wda import WDA
from config import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD

wdamodel = WDA(
    db_host=DB_HOST,
    db_port=DB_PORT,
    db_username=DB_USERNAME,
    db_password=DB_PASSWORD,
)
