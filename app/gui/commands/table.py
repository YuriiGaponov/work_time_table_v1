"""
Команды взаимодействия графического интерфейса
с другими пакетами при работе с табелями.
"""

from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import List, Optional

from app.calendar.models import CalendarDay
from app.gui.views.table_views.schemas import TableSearchSchema


def get_search_data(
        year: str, month: str, department: str
) -> TableSearchSchema:
    """
    Возвращает данные введенные данные в формате,
    используемом для построения табеля.
    """
    return {
        'year': year,
        'month': month,
        'department': department
    }


def get_table_days(
        db: Session, data: TableSearchSchema
) -> Optional[List[CalendarDay]]:
    """Принимает год и месяц, возвращает дни месяца из БД."""

    return db.query(CalendarDay).filter(
        and_(
            CalendarDay.year == data['year'],
            CalendarDay.month == data['month']
        )
    )


def get_table(db: Session, year: str, month: str, department: str):
    return get_table_days(db, get_search_data(year, month, department))
