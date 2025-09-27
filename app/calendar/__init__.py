"""
Пакет для работы с классами календарей, используемых при построении тебелей.
"""

from .main import save_calendar
from .models import WorkDay

__all__ = [
    'save_calendar',
    'WorkDay'
]
