from .constants import ConsultantPlusParserConfig
from .interfaces import ParserInterface, ParserConfigInterface
from .parser import ConsultantPlusParser


class Settings():
    """Вабор класса парсера."""

    PARSER: ParserInterface = ConsultantPlusParser
    PARSER_CONFIG: ParserConfigInterface = ConsultantPlusParserConfig
