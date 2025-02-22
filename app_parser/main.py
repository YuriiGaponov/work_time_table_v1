from constants import MAIN_URL
from utils import get_soup


def main():
    """Главная функция парсера."""
    soup = get_soup(MAIN_URL)
    print(soup)


if __name__ == '__main__':
    main()
