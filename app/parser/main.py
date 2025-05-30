from typing import List, Tuple

from .config import ConsultantPlusParserConfig
from .interfaces import ParserInterface
from .parser import ConsultantPlusParser

# Инициализированнный объект конфигурации парсера.
parser_config = ConsultantPlusParserConfig()

# Парсер производственного календаря.
parser = ConsultantPlusParser(parser_config)


def parse_calendar(
    parser: ParserInterface
) -> List[Tuple[int, int, str, int, bool]]:
    """Главная функция парсера."""
    return parser.get_calendar()


if __name__ == '__main__':
    parse_calendar()
