from .calendar import CalendarDay # noqa
from .db import Base, engine
from .parser import parser


def main():
    """Главная функция приложения."""
    return parser()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    main()
