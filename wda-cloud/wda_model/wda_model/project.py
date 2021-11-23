#!/usr/bin/env python3
# coding:utf-8
import datetime
from sqlalchemy import Integer, Column, String, DateTime
from .base import Base, BaseModel


class BaseProject(object):
    keys = ["id", "uid", "username", "name", "creat_date", "company", "update_date", "type", "note", "status",
            "version", "descript", "background", "app1", "app2", "app3"]
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(String(64), nullable=True)
    username = Column(String(256), nullable=True)
    group = Column(String(256), nullable=True)
    company = Column(String(256), nullable=True)
    creat_date = Column(DateTime, default=datetime.datetime.utcnow)
    update_date = Column(DateTime, default=datetime.datetime.utcnow)
    master = Column(String(64), nullable=True)
    type = Column(String(64), nullable=True)
    name = Column(String(256), nullable=True)
    note = Column(String(1000), nullable=True)
    status = Column(String(32), nullable=True)
    version = Column(String(64), nullable=True, default="0")
    delete = Column(Integer, nullable=True, default=0)
    descript = Column(String(512), nullable=True)
    background = Column(String(512), nullable=True)  # 背景图片路径
    app1 = Column(String(64), nullable=True)
    app2 = Column(String(64), nullable=True)
    app3 = Column(String(64), nullable=True)


class Project(Base, BaseProject, BaseModel):
    __tablename__ = 'project'


class LayoutProject(Base, BaseProject, BaseModel):
    __tablename__ = 'layout_project'


class Layout2Project(Base, BaseProject, BaseModel):
    """
    layout v2
    """
    __tablename__ = 'layout2_project'


class ResourceModelProject(Base, BaseProject, BaseModel):
    __tablename__ = 'resource_model_project'


class DataAnalyticsProject(Base, BaseProject, BaseModel):
    __tablename__ = 'data_analytics_project'


class CadProject(Base, BaseProject, BaseModel):
    __tablename__ = 'cad_project'
