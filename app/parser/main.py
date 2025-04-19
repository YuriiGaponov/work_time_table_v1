import re
from bs4 import BeautifulSoup
from bs4.element import Tag

from .constants import (
    DAY_PATTERN,
    DAY_INDEX_PATTERN,
    MAIN_URL,
    YEAR_PATTERN,
    WEEKEND_PATTERN
)
from .utils import get_days_tag, get_month_table, get_soup


def get_year(soup: BeautifulSoup) -> int:
    """Возвращает год календаря в виде числа."""
    return int(re.search(YEAR_PATTERN, soup.find('h1').text).group('year'))


def get_month(month: Tag) -> str:
    """Возвращает месяц в виде строки."""
    return month.find('th', {'class': 'month'}).text


def get_day(day: Tag) -> int:
    """Возвращает число месяца."""
    return int(re.search(DAY_INDEX_PATTERN, day.text).group('day'))


def is_weekend(day: Tag) -> bool:
    """
    Возращает "выходной", если день является выходным или праздничным,
    в остальных случаях возвращает "рабочий".
    """
    return 'выходной' if WEEKEND_PATTERN in day['class'] else 'рабочий'


def main():
    """Главная функция парсера."""
    soup = get_soup(MAIN_URL)
    year = get_year(soup)
    day_count = 0
    for month in get_month_table(soup):
        month_title = get_month(month)
        for day in get_days_tag(month):
            if DAY_PATTERN.match(day.text):
                day_count += 1
                day_nuber = get_day(day)
                weekend = is_weekend(day)
                print((day_count, day_nuber, month_title, year, weekend))


if __name__ == '__main__':
    main()
