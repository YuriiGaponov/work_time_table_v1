import logging

from ..core import app_settings

# Логгер парсера
logger = logging.getLogger(__name__)

# Хэндлер парсера
handler = logging.FileHandler(
    f'{app_settings.LOG_PATH}{__name__}.log',
    mode='w', encoding=app_settings.LOG_ENCODING
)

# Формат записей логов парсера
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
