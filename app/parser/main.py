from .constants import parser_constants
from .parser import Parser

# Парсер производственного календаря.
parser = Parser(parser_constants.MAIN_URL)


def main():
    """Главная функция парсера."""
    return parser.get_calendar()


if __name__ == '__main__':
    main()
