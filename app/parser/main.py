from typing import List, Tuple

from .interfaces import ParserInterface
from .services import get_parser
from .settings import Settings


def parse_calendar(
    year: str,
) -> List[Tuple[int, int, str, int, bool]]:
    """Главная функция парсера."""
    parser: ParserInterface = get_parser(
        year, Settings.PARSER_CONFIG, Settings.PARSER
    )
    return parser.get_calendar()


if __name__ == '__main__':
    parse_calendar()
