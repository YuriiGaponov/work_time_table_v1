"""
Модели для хранения сведений о днях года,
о количестве отработанного времени в конкретный день конкретным сотрудником.
"""

from sqlalchemy import Boolean, Column, Integer, String, UniqueConstraint

from app.db import Base


class CalendarDay(Base):
    """Класс для хранения сведений о дне года."""

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    number: int = Column(Integer)
    day: int = Column(Integer)
    month: str = Column(String)
    year: int = Column(Integer)
    is_weekend: bool = Column(Boolean)

    __table_args__ = (
        UniqueConstraint('number', 'day', 'month', 'year', 'is_weekend',
                         name='ux_calendar_day'),
    )

    def __init__(self, number, day, month, year, is_weekend):
        """Конструктор для создания дня года."""
        self.number = number
        self.day = day
        self.month = month
        self.year = year
        self.is_weekend = is_weekend


class TableDay(Base):
    """Класс для хранения информации о рабочем дне сотрудника."""

    id: int = Column(Integer, primary_key=True, autoincrement=True)
