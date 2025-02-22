import requests
from bs4 import BeautifulSoup


def get_soup(url: str, parser: str = 'lxml') -> BeautifulSoup:
    """
    Принимает на вход url страницы и парсер (по умолчанию используется lxml),
    возвращает HTML страницы в виде текста.
    """
    return BeautifulSoup(requests.Session().get(url).text, parser)
