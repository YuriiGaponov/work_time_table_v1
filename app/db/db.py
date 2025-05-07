from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr

from .settings import db_settings

engine = create_engine(db_settings.get_db_connection())


class PreBase():
    """Класс предустановленных параметров базы данных."""

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)
