"""
Схемы данных, используемые при обработке табелей.
"""

from typing import TypedDict


class TableSearchSchema(TypedDict):
    """Строго типизированный словарь параметров для поиска табеля в БД."""

    year: str
    month: str
    department: str
