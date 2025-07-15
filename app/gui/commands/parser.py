from ...calendar import save_calendar
from ...db import session
from ...parser import parse_calendar, parser


# Функция выведена временно и будет переработана
def get_calendar():
    """Запуск парсера производственного календаря."""
    save_calendar(session, parse_calendar(parser))
