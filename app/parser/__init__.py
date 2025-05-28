# Инициализация модуля, экспорт основного парсера
from .main import main as parser

# Экспортируемые имена
__all__ = ['parser']

if __name__ == '__main__':
    parser()
