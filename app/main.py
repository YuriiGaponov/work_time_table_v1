from .calendar import save_calendar
from .db import Base, engine, session
from .parser import parse_calendar, parser


def main() -> None:
    """Главная функция приложения."""
    return save_calendar(session, parse_calendar(parser))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
