import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def get_soup(url: str, parser: str = 'lxml') -> BeautifulSoup:
    """
    Принимает на вход url страницы и парсер (по умолчанию используется lxml),
    возвращает HTML страницы в виде текста.
    """
    return BeautifulSoup(requests.Session().get(url).text, parser)


def get_month_table(soup: BeautifulSoup) -> list:
    """Возвращает список тэгов календаря для каждого месяца."""
    return soup.find_all('table', {'class': 'cal'})


def get_days_tag(month: Tag) -> list:
    """Возвращает список тэгов дней в месяце."""
    return month.find_all('td')
