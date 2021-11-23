#!/usr/bin/env python3
# coding:utf-8
from sqlalchemy import create_engine


def init_engine(host, port, username, password, dbname):
    db_config = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(
        db_config
    )
    return engine
