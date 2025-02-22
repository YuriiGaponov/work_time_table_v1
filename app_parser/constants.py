import re

MAIN_URL = 'https://www.consultant.ru/law/ref/calendar/proizvodstvennye/2025/'

# Шаблон для поиска года в тексте тэга.
YEAR_PATTERN = re.compile(r'Производственный календарь на (?P<year>\d{4}) год')
