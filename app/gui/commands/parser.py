from app.calendar import save_calendar
from app.db import session
from app.parser import parse_calendar


def get_calendar(year: str) -> None:
    """
    Запуск парсера производственного календаря,
    сохранение дней календаря в БД.
    """
    save_calendar(session, parse_calendar(year))
