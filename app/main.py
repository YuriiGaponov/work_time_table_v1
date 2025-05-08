from .calendar import save_calendar
from .db import Base, engine, session
from .parser import parser


def main():
    """Главная функция приложения."""
    return save_calendar(session, parser())


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
