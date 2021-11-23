#!/usr/bin/env python3
# coding:utf-8
from .project import Project, LayoutProject, ResourceModelProject, DataAnalyticsProject, Layout2Project, CadProject
from .layout import LayoutFile, LayoutCacheFile
from .db import init_engine


class WDA(object):
    db_host = "127.0.0.1"
    db_port = 5432
    db_name = "shucheng"
    db_username = "admin"
    db_password = "admin"
    db_engine = None
    project = Project
    layout_project = LayoutProject
    layout2_project = Layout2Project
    cad_project = CadProject
    resource_model_project = ResourceModelProject
    data_analytics_project = DataAnalyticsProject
    layout_file = LayoutFile
    layout_cache_file = LayoutCacheFile

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
        self.init_table()

    def init_db(self):
        engine = init_engine(
            host=self.db_host,
            port=self.db_port,
            username=self.db_username,
            password=self.db_password,
            dbname=self.db_name,
        )
        self.db_engine = engine

    def init_table(self):
        self.project.init(self.db_engine)
        self.layout_project.init(self.db_engine)
        self.resource_model_project.init(self.db_engine)
        self.data_analytics_project.init(self.db_engine)
        self.layout_file.init(self.db_engine)
        self.layout_cache_file.init(self.db_engine)
        self.layout2_project.init(self.db_engine)
        self.cad_project.init(self.db_engine)
