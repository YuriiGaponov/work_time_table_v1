from sqlalchemy import Boolean, Column, Integer, String

from ..db import Base


class CalendarDay(Base):
    number: int = Column(Integer)
    day: int = Column(Integer)
    month: str = Column(String)
    year: int = Column(Integer)
    is_weekend: bool = Column(Boolean)
