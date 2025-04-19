import re

MAIN_URL = 'https://www.consultant.ru/law/ref/calendar/proizvodstvennye/2025/'

# Шаблон для поиска года в тексте тэга.
YEAR_PATTERN = re.compile(r'Производственный календарь на (?P<year>\d{4}) год')

# Шаблоны для поиска числа месяца в тексте тэга.
DAY_PATTERN = re.compile(r'^\d{1,2}\*?')
DAY_INDEX_PATTERN = re.compile(r'^(?P<day>\d{1,2})')
WEEKEND_PATTERN = 'weekend'
