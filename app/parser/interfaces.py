from typing import List, Protocol, Tuple


class ParserInterface(Protocol):
    """Интерфейс парсера."""

    def get_calendar() -> List[Tuple[int, int, str, int, bool]]:
        """Возвращает результаты парсинга производственного календаряя."""


class ParserConfigInterface(Protocol):
    """Интерфейс настроек парсера."""

    MAIN_URL: str
