import re
from bs4 import BeautifulSoup

from constants import MAIN_URL, YEAR_PATTERN
from utils import get_soup


def get_year(soup: BeautifulSoup) -> int:
    """Возвращает год календаря в виде числа."""
    return int(re.search(YEAR_PATTERN, soup.find('h1').text).group('year'))


def main():
    """Главная функция парсера."""
    soup = get_soup(MAIN_URL)
    year = get_year(soup)
    print(year)


if __name__ == '__main__':
    main()
