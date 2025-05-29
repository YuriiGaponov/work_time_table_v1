from .config import ConsultantPlusParserConfig
from .parser import ConsultantPlusParser

# Инициализированнный объект конфигурации парсера.
parser_config = ConsultantPlusParserConfig()

# Парсер производственного календаря.
parser = ConsultantPlusParser(parser_config)


def main():
    """Главная функция парсера."""
    return parser.get_calendar()


if __name__ == '__main__':
    main()
