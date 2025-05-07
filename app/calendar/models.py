from sqlalchemy import Column, Integer

from ..db import Base


class CalendarDay(Base):
    number: int = Column(Integer)
