from .config import ConsultantPlusParserConfig as ParserConfig
from .main import parse_calendar
from .parser import ConsultantPlusParser as Parser

__all__ = ['parse_calendar', 'ParserConfig', 'Parser']
