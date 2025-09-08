from app.calendar import save_calendar
from app.db import session
from app.gui.views import BaseView
from app.parser import parse_calendar


def open_year_selector(top_view: BaseView) -> None:
    """Открыть окно выбора года производственного календаря."""
    from app.gui.views import YearSelectorView
    year_selector = YearSelectorView(top_view)
    year_selector.run()


def open_incorrect_year(info: str, top_view: BaseView) -> None:
    """Открыть окно с указанием ошибки ввода года."""
    from app.gui.views import IncorrectYearView
    incorrect_year = IncorrectYearView(top_view)
    incorrect_year.root_head_lable.config(text=info)
    incorrect_year.run()


def get_calendar(year: str) -> None:
    """
    Запуск парсера производственного календаря,
    сохранение дней календаря в БД.
    """
    save_calendar(session, parse_calendar(year))
