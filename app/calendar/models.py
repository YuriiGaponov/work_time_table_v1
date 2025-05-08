from sqlalchemy import Boolean, Column, Integer, String

from ..db import Base


class CalendarDay(Base):
    """Класс для хранения сведений о дне года."""

    number: int = Column(Integer)
    day: int = Column(Integer)
    month: str = Column(String)
    year: int = Column(Integer)
    is_weekend: bool = Column(Boolean)

    def __init__(self, number, day, month, year, is_weekend):
        self.number = number
        self.day = day
        self.month = month
        self.year = year
        self.is_weekend = is_weekend
