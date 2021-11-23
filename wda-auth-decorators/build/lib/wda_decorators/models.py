#!/usr/bin/env python3
# coding:utf-8
import datetime
from sqlalchemy import Integer, Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BaseModel(object):
    keys = []

    def __init__(self, id, engine, obj):
        data = obj.get(id, engine)
        if data:
            for k in self.keys:
                v = getattr(data, k)
                setattr(self, k, v)
        else:
            self.id = -1

    @classmethod
    def init(cls, engine):
        if not cls.is_table_exists(engine):
            cls.__table__.create(engine)

    @classmethod
    def is_table_exists(cls, engine):
        name = cls.__tablename__
        res = engine.dialect.has_table(engine, name)
        return res

    @classmethod
    def create_session(cls, engine):
        db_session = sessionmaker(bind=engine)()
        return db_session

    @classmethod
    def get(cls, id, engine):
        db_session = cls.create_session(engine)
        data = db_session.query(cls).filter(cls.id == id)
        data = list(data)
        db_session.close()
        if data:
            return data[0]
        else:
            return None


class Session(Base, BaseModel):
    __tablename__ = 'django_session'
    session_key = Column(String(40), primary_key=True)
    session_data = Column(String(256))

    @classmethod
    def get_session(cls, sessionid, engine):
        db_session = cls.create_session(engine)
        data = db_session.query(cls).filter(cls.session_key == sessionid)
        data = list(data)
        db_session.close()
        if data:
            return data[0]
        else:
            return None


class User(Base, BaseModel):
    keys = ["id", "is_superuser", "username", "is_staff", "is_active"]
    __tablename__ = 'auth_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(128))
    last_login = Column(DateTime)
    is_superuser = Column(Boolean)
    username = Column(String(150))
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(254))
    is_staff = Column(Boolean)
    is_active = Column(Boolean)
    date_joined = Column(DateTime)

    def __init__(self, uid, engine):
        BaseModel.__init__(self, uid, engine, User)

    def get_groups(self, engine):
        return UserGroups.get_user_groups(self.id, engine)

    def get_permissions(self, engine):
        return UserPermissions.get_user_permissions(self.id, engine)


class Permission(Base, BaseModel):
    keys = ["id", "name", "content_type_id", "codename"]
    __tablename__ = 'auth_permission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256))
    content_type_id = Column(Integer)
    codename = Column(String(100))

    def __init__(self, id, engine):
        BaseModel.__init__(self, id, engine, Permission)


class Group(Base, BaseModel):
    keys = ["id", "name"]
    __tablename__ = 'auth_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150))

    def __init__(self, id, engine):
        BaseModel.__init__(self, id, engine, Group)


class UserGroups(Base, BaseModel):
    __tablename__ = 'auth_user_groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    group_id = Column(Integer)

    @classmethod
    def get_user_groups(cls, uid, engine):
        groups = {"": 1}
        db_session = cls.create_session(engine)
        data = db_session.query(cls).filter(cls.user_id == uid)
        data = list(data)
        db_session.close()

        for _data in data:
            group = Group(_data.group_id, engine)
            groups[group.name] = group.id

        return groups


class UserPermissions(Base, BaseModel):
    __tablename__ = 'auth_user_user_permissions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    permission_id = Column(Integer)

    @classmethod
    def get_user_permissions(cls, uid, engine):
        permissions = {"": 1}
        db_session = cls.create_session(engine)
        data = db_session.query(cls).filter(cls.user_id == uid)
        data = list(data)
        db_session.close()
        for _data in data:
            permission = Permission(_data.permission_id, engine)
            permissions[permission.codename] = {
                "id": permission.id,
                "name": permission.name,
            }

        return permissions


class UserInfo(Base, BaseModel):
    """
    email = models.CharField(max_length=128, default="")
    tel = models.CharField(max_length=64, default="")
    name = models.CharField(max_length=256, null=True)
    username = models.CharField(max_length=256, null=True)
    company_name = models.CharField(max_length=256, null=True)
    company_homepage = models.CharField(max_length=256, null=True)
    company_position = models.CharField(max_length=256, null=True)
    text = models.CharField(max_length=512, null=True)
    country = models.CharField(max_length=128, null=True)
    create_date = models.DateTimeField(null=True)
    type = models.CharField(max_length=128, default="")  # personal / enterprise
    business_type = models.CharField(max_length=128, default="")  # A / B
    user_id = models.IntegerField(null=True)
    level = models.IntegerField(default=0)
    expired = models.DateField(null=True)
    begin = models.DateField(null=True)
    first_day = models.CharField(max_length=128, null=True)
    limit = models.IntegerField(default=10)
    """
    keys = ["id", "user_id", "username", "type", "business_type", "level", "expired", "limit"]
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(128))
    tel = Column(String(64))
    name = Column(String(256))
    username = Column(String(256))
    company_name = Column(String(256))
    company_homepage = Column(String(256))
    company_position = Column(String(256))
    text = Column(String(512))
    country = Column(String(128))
    create_date = Column(DateTime)
    type = Column(String(128))
    business_type = Column(String(128))
    user_id = Column(Integer)
    level = Column(Integer)
    expired = Column(DateTime)
    begin = Column(DateTime)
    first_day = Column(String(128))
    limit = Column(Integer)

    def __init__(self, id, engine):
        BaseModel.__init__(self, id, engine, UserInfo)

    def json(self):
        data = {}
        if not self.id > 0:
            return None
        for k in self.keys:
            data[k] = getattr(self, k)
        data["expired"] = f"{data['expired']}"
        return data

    def is_expired(self):
        if self.expired > datetime.date.today():
            return -1
        else:
            return 1
