# Python 3.7.2, SQLAlchemy 1.3.13
###
# app/models.py
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

class Base(object):
    @classmethod
    def __table_cls__(cls, *args, **kwargs):
        t = Table(*args, **kwargs)
        t.decl_class = cls
        return t

Base = declarative_base(cls=Base)
