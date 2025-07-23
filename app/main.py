from app.core import app_settings
from app.db import Base, engine
from app.gui import MainView


def main() -> None:
    """Главная функция приложения."""
    app = MainView()
    app.run()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app_settings.check_dirs()
    main()
