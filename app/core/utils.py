import os
import sys


def get_path(relative_path: str) -> str:
    """
    В зависимости от способа запуска приложения:
    - исполняемая папка / файл
    - через терминал на этапе разработки
    возвращает абсолютный путь.
    """
    try:
        # Для исполняемого файла
        base_path = sys._MEIPASS
    except Exception:
        # Для разработки
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
