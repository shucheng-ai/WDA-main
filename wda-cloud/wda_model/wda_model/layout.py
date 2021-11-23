#!/usr/bin/env python3
# coding:utf-8
import datetime
from sqlalchemy import Integer, Column, String, DateTime
from .base import Base, BaseModel


class LayoutFile(Base, BaseModel):
    """
    上传文件，永久保存
    """
    __tablename__ = 'layout_file'
    keys = ["id", "uid", "hash", "project_id", "filename", "company", "username", "creat_date", "type", "path"]
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String(256), nullable=True)
    uid = Column(String(64), nullable=True)
    project_id = Column(String(64), nullable=True)
    filename = Column(String(256), nullable=True)
    username = Column(String(256), nullable=True)
    company = Column(String(256), nullable=True)
    creat_date = Column(DateTime, default=datetime.datetime.utcnow)
    type = Column(String(64), nullable=True)
    path = Column(String(512), nullable=True)


class LayoutCacheFile(Base, BaseModel):
    """
    上传文件，临时存储，定期删除
    """
    __tablename__ = 'layout_cache_file'
    keys = ["id", "uid", "hash", "project_id", "filename", "company", "username", "creat_date", "type", "path"]
    id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(String(256), nullable=True)
    uid = Column(String(64), nullable=True)
    project_id = Column(String(64), nullable=True)
    filename = Column(String(256), nullable=True)
    username = Column(String(256), nullable=True)
    company = Column(String(256), nullable=True)
    creat_date = Column(DateTime, default=datetime.datetime.utcnow)
    type = Column(String(64), nullable=True)
    path = Column(String(512), nullable=True)
