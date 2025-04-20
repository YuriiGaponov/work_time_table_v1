from .constants import parser_constants
from .parser import Parser

# Парсер производственного календаря.
parser = Parser(parser_constants.MAIN_URL)


def main():
    """Главная функция парсера."""
    for date in parser.get_calendar():
        print(date)


if __name__ == '__main__':
    main()
