#!/usr/bin/env python3
# coding:utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BaseModel(object):
    keys = []

    @classmethod
    def init(cls, engine):
        if not cls.is_table_exists(engine):
            cls.__table__.create(engine)

    @classmethod
    def is_table_exists(cls, engine):
        name = cls.__tablename__
        res = engine.dialect.has_table(engine, name)
        print(f"table {name} is {res}")
        return res

    @classmethod
    def create_session(cls, engine):
        db_session = sessionmaker(bind=engine)()
        return db_session

    @classmethod
    def get_maxid(cls, engine):
        dbsession = cls.create_session(engine)
        maxid = dbsession.query(cls).order_by(cls.id.desc()).first()
        dbsession.close()
        if maxid:
            return maxid.id
        else:
            return 0

    @classmethod
    def add(cls, data, engine):
        res = {}
        dbsession = cls.create_session(engine)
        dbsession.add(data)
        dbsession.commit()
        dbsession.flush()
        res['id'] = data.id
        dbsession.close()
        return res

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

    @classmethod
    def remove(cls, id, engine):
        cls.update(id=id, engine=engine, data={"delete": 1})

    @classmethod
    def update(cls, id, data={}, engine=None):
        db_session = cls.create_session(engine)
        for k, v in data.items():
            obj = db_session.query(cls).filter(cls.id == id).one()
            setattr(obj, k, v)
        db_session.commit()
        db_session.flush()
        db_session.close()
        return

    @classmethod
    def filter(cls, offset=0, limit=10, order_by='id', reverse=False, engine=None, fliters=None):
        db_session = cls.create_session(engine)
        if not fliters:
            fliters = {}
        if reverse:
            results = db_session.query(cls).filter_by(**fliters).order_by(getattr(cls, order_by).desc()).limit(
                limit).offset(offset).all()
        else:
            results = db_session.query(cls).filter_by(**fliters).order_by(getattr(cls, order_by)).limit(limit).offset(
                offset).all()
        db_session.close()
        return results

    @classmethod
    def count(cls, fliters: dict = {}, engine=None):
        db_session = cls.create_session(engine)
        results = db_session.query(cls).filter_by(**fliters).count()
        db_session.close()
        return results

    @classmethod
    def json(cls, obj):
        data = {}
        for k in cls.keys:
            if getattr(obj, k):
                v = f'{getattr(obj, k)}'
            else:
                v = ''
            data[k] = v
        return data
