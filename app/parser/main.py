from .constants import parser_constants
from .parser import Parser

# Парсер производственного календаря.
parser = Parser(parser_constants.MAIN_URL)


def main():
    """Главная функция парсера."""
    year = parser.get_year()
    day_count = 0
    for month in parser.get_month_table():
        month_title = parser.get_month_title(month)
        for day in parser.get_days_tag(month):
            if parser_constants.DAY_PATTERN.match(day.text):
                day_count += 1
                day_nuber = parser.get_day(day)
                weekend = 'выходной' if parser.is_weekend(day) else 'рабочий'
                print((day_count, day_nuber, month_title, year, weekend))


if __name__ == '__main__':
    main()
