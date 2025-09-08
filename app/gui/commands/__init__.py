"""
Пакет команд для открытия окон приложения
и взаимодействия графического интерфейса с другими пакетами.
"""

from app.employees import search_employees
from .employees import create_employee
from .parser import get_calendar
from .validators import not_validate_year
from .views import (
    open_info_view,
    open_modal_view,
    open_search_view
)

__all__ = [
    'create_employee',
    'get_calendar',
    'not_validate_year',
    'open_info_view',
    'open_modal_view',
    'open_search_view',
    'search_employees'
]
