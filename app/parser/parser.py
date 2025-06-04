import re
import requests
from dataclasses import dataclass
from typing import List, Optional, Tuple

from bs4 import BeautifulSoup
from bs4.element import Tag

from .config import ConsultantPlusParserConfig
from .logger import logger


@dataclass
class ConsultantPlusParser():
    """
    Класс парсера производственного календаря
    для сайта Консультант+.
    """

    config: ConsultantPlusParserConfig
    _soup: Optional[BeautifulSoup] = None

    def _get_soup(self, parser: str = 'lxml') -> BeautifulSoup:
        """
        Принимает на вход url страницы и парсер
        (по умолчанию используется lxml),
        возвращает HTML страницы в виде текста.
        """
        if self._soup is None:
            logger.info(f'Получение HTML со страницы \n{self.config.MAIN_URL}')
            self._soup = BeautifulSoup(
                requests.Session().get(self.config.MAIN_URL).text, parser
            )
        return self._soup

    def _get_year(self) -> int:
        """Возвращает год календаря."""
        return int(re.search(
            self.config.YEAR_PATTERN, self._get_soup().find('h1').text
        ).group('year'))

    def _get_month_table(self) -> List[Tag]:
        """Возвращает список тэгов календаря для каждого месяца."""
        return self._get_soup().find_all('table', {'class': 'cal'})

    def _get_month_title(self, month: Tag) -> str:
        """Возвращает название месяца."""
        return month.find('th', {'class': 'month'}).text

    def _get_days_tag(self, month: Tag) -> List[Tag]:
        """Возвращает список тэгов дней в месяце."""
        return month.find_all('td')

    def _get_day(self, day: Tag) -> int:
        """Возвращает число месяца."""
        return int(re.search(
            self.config.DAY_INDEX_PATTERN, day.text
        ).group('day'))

    def _is_weekend(self, day: Tag) -> bool:
        """Возращает True, если день является выходным или праздничным."""
        return self.config.WEEKEND_PATTERN in day['class']

    def get_calendar(self) -> List[Tuple[int, int, str, int, bool]]:
        """
        Возвращает список дней года в виде:
        номер дня в году, число, название месяца, год, является ли выходным.
        """
        result = []
        year = self._get_year()
        day_count = 0
        for month in self._get_month_table():
            month_title = self._get_month_title(month)
            for day in self._get_days_tag(month):
                if self.config.DAY_PATTERN.match(day.text):
                    day_count += 1
                    result.append(
                        (
                            day_count,
                            self._get_day(day),
                            month_title, year,
                            self._is_weekend(day)
                        )
                    )
        return result
