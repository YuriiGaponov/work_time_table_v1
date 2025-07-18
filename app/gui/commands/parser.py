from ...calendar import save_calendar
from ...db import session
from ...parser import parse_calendar, Parser, ParserConfig


def open_year_selector() -> None:
    """Открыть окно выбора года производственного календаря."""
    from ..views import YearSelectorView
    year_selector = YearSelectorView()
    year_selector.run()


def get_calendar_url(year: str) -> ParserConfig:
    """Добавляет в url парсера год календаря."""
    config = ParserConfig()
    main_url = config.MAIN_URL
    config.MAIN_URL = f'{main_url}{year}/'
    return config


def get_parser(year: str) -> Parser:
    """Создает экземпляр парсера производственного календаря."""
    return Parser(get_calendar_url(year))


def get_calendar(year: str) -> None:
    """Запуск парсера производственного календаря."""
    save_calendar(session, parse_calendar(get_parser(year)))
