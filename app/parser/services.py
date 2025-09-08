from .interfaces import ParserInterface, ParserConfigInterface


def get_calendar_url(
        year: str,
        config: ParserConfigInterface
) -> ParserConfigInterface:
    """Добавляет в url парсера год календаря."""
    config.MAIN_URL = f'{config.MAIN_URL}{year}/'
    return config


def get_parser(
        year: str,
        config: ParserConfigInterface,
        ParserClass: ParserInterface
) -> ParserInterface:
    """Создает экземпляр парсера производственного календаря."""
    return ParserClass(get_calendar_url(year, config))
