"""
Схемы данных, используемые при обработке табелей.
"""

from typing import List, Optional, TypedDict

from app.calendar.models import CalendarDay
from app.employees.models import Employee


class TableSearchSchema(TypedDict):
    """Строго типизированный словарь параметров для поиска табеля в БД."""

    year: str
    month: str
    department: str


class TableDataSchema(TypedDict):
    """Строго типизированный словарь данных для построения табеля."""

    table_days: Optional[List[CalendarDay]]
    employees: Optional[List[Employee]]
