from ...calendar import save_calendar
from ...db import session
from ...parser import parse_calendar, Parser, ParserConfig
from ..views import BaseView


def open_year_selector(top_view: BaseView) -> None:
    """Открыть окно выбора года производственного календаря."""
    from ..views import YearSelectorView
    year_selector = YearSelectorView(top_view)
    year_selector.run()


def open_incorrect_year(info: str, top_view: BaseView) -> None:
    """Открыть окно с указанием ошибки ввода года."""
    from ..views import IncorrectYearView
    incorrect_year = IncorrectYearView(top_view)
    incorrect_year.root_head_lable.config(text=info)
    incorrect_year.run()


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
