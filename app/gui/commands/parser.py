from ...calendar import save_calendar
from ...db import session
from ...parser import parse_calendar, parser, ParserConfig


# Функция выведена временно и будет переработана
def get_calendar():
    """Запуск парсера производственного календаря."""
    save_calendar(session, parse_calendar(parser))


def open_year_selector():
    """Открыть окно выбора года производственного календаря."""
    from ..views import ParserYearSelector
    year_selector = ParserYearSelector()
    year_selector.run()


def get_calendar_url(year: str) -> str:
    """Добавляет в url парсера год календаря."""
    config = ParserConfig()
    main_url = config.MAIN_URL
    # return f'{main_url}{year}/'
    print(f'{main_url}{year}/')
