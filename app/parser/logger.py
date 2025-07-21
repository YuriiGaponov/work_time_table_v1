import logging
from pathlib import Path

from app.core import app_settings

# Путь к директории логов
log_dir = Path(app_settings.LOG_PATH)

# Проверяем существование директории логов и создаем её, если нужно
if not log_dir.exists():
    log_dir.mkdir(parents=True, exist_ok=True)

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
