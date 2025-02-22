import requests
from bs4 import BeautifulSoup

from constants import MAIN_URL


def main():
    """Главная функция парсера."""
    session = requests.Session()
    response = session.get(MAIN_URL)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)


if __name__ == '__main__':
    main()
