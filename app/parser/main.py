import re
from bs4 import BeautifulSoup
from bs4.element import Tag

from .constants import parser_constants
from .utils import get_days_tag, get_month_table, get_soup


def get_year(soup: BeautifulSoup) -> int:
    """Возвращает год календаря в виде числа."""
    return int(re.search(
        parser_constants.YEAR_PATTERN, soup.find('h1').text
    ).group('year'))


def get_month(month: Tag) -> str:
    """Возвращает месяц в виде строки."""
    return month.find('th', {'class': 'month'}).text


def get_day(day: Tag) -> int:
    """Возвращает число месяца."""
    return int(re.search(
        parser_constants.DAY_INDEX_PATTERN, day.text
    ).group('day'))


def is_weekend(day: Tag) -> bool:
    """Возращает True, если день является выходным или праздничным."""
    return parser_constants.WEEKEND_PATTERN in day['class']


def main():
    """Главная функция парсера."""
    soup = get_soup(parser_constants.MAIN_URL)
    year = get_year(soup)
    day_count = 0
    for month in get_month_table(soup):
        month_title = get_month(month)
        for day in get_days_tag(month):
            if parser_constants.DAY_PATTERN.match(day.text):
                day_count += 1
                day_nuber = get_day(day)
                weekend = 'выходной' if is_weekend(day) else 'рабочий'
                print((day_count, day_nuber, month_title, year, weekend))


if __name__ == '__main__':
    main()
