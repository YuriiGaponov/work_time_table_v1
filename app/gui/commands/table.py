"""
Команды взаимодействия графического интерфейса
с другими пакетами при работе с табелями.
"""

from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import List, Optional

from app.calendar.models import CalendarDay
from app.employees.models import Employee
from app.gui.views.table_views.schemas import (
    TableDataSchema,
    TableSearchSchema
)


def get_search_data(
        year: str, month: str, department: str
) -> TableSearchSchema:
    """
    Возвращает введенные данные в формате,
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
    """
    Принимает данные в формате, используемом для построения табеля,
    используя из них год и месяц, возвращает список календарных дней из БД.
    """

    return db.query(CalendarDay).filter(
        and_(
            CalendarDay.year == data['year'],
            CalendarDay.month == data['month']
        )
    )


def get_employees(
        db: Session, data: TableSearchSchema
) -> Optional[List[Employee]]:
    """
    Принимает данные в формате, используемом для построения табеля,
    используя из них год и месяц, возвращает список календарных дней из БД.
    """

    return db.query(Employee).filter(
        and_(
            Employee.department == data['department']
        )
    )


def get_table(
        db: Session, year: str, month: str, department: str
) -> TableDataSchema:
    table_data = get_search_data(year, month, department)
    return {
        'table_days': get_table_days(db, table_data),
        'employees': get_employees(db, table_data)
    }
