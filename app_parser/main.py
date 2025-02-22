import re
from bs4 import BeautifulSoup
from bs4.element import Tag

from constants import DAY_PATTERN, DAY_INDEX_PATTERN, MAIN_URL, YEAR_PATTERN
from utils import get_days_tag, get_month_table, get_soup


def get_year(soup: BeautifulSoup) -> int:
    """Возвращает год календаря в виде числа."""
    return int(re.search(YEAR_PATTERN, soup.find('h1').text).group('year'))


def get_month(month: Tag) -> str:
    """Возвращает месяц в виде строки."""
    return month.find('th', {'class': 'month'}).text


def get_day(day: Tag) -> int:
    """Возвращает число месяца."""
    return int(re.search(DAY_INDEX_PATTERN, day.text).group('day'))


def main():
    """Главная функция парсера."""
    soup = get_soup(MAIN_URL)
    month_table = get_month_table(soup)
    year = get_year(soup)
    for month in month_table:
        month_title = get_month(month)
        for day in get_days_tag(month):
            if DAY_PATTERN.match(day.text):
                print((get_day(day), month_title, year))


if __name__ == '__main__':
    main()
