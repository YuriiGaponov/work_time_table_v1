import re
import requests

from bs4 import BeautifulSoup
from bs4.element import Tag

from .constants import parser_constants


class Parser():
    """Класс парсера производственного календаря."""

    def __init__(self, url: str):
        self.url = url

    def get_soup(self, parser: str = 'lxml') -> BeautifulSoup:
        """
        Принимает на вход url страницы и парсер
        (по умолчанию используется lxml),
        возвращает HTML страницы в виде текста.
        """
        return BeautifulSoup(requests.Session().get(self.url).text, parser)

    def get_year(self) -> int:
        """Возвращает год календаря в виде числа."""
        return int(re.search(
            parser_constants.YEAR_PATTERN, self.get_soup().find('h1').text
        ).group('year'))

    def get_month_table(self) -> list:
        """Возвращает список тэгов календаря для каждого месяца."""
        return self.get_soup().find_all('table', {'class': 'cal'})

    def get_month_title(self, month: Tag) -> str:
        """Возвращает название месяца в виде строки."""
        return month.find('th', {'class': 'month'}).text

    def get_days_tag(self, month: Tag) -> list:
        """Возвращает список тэгов дней в месяце."""
        return month.find_all('td')

    def get_day(self, day: Tag) -> int:
        """Возвращает число месяца."""
        return int(re.search(
            parser_constants.DAY_INDEX_PATTERN, day.text
        ).group('day'))

    def is_weekend(self, day: Tag) -> bool:
        """Возращает True, если день является выходным или праздничным."""
        return parser_constants.WEEKEND_PATTERN in day['class']
