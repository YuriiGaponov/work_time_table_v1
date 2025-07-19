from .parser import open_incorrect_year


def validate_year(year: str) -> bool:
    """Валидирует значение, переданное в поле года."""
    if not year:
        open_incorrect_year('Ошибка: год не может быть пустым')
        return False

    # Проверка на наличие только цифр
    if not year.isdigit():
        open_incorrect_year("Ошибка: год должен содержать только цифры")
        return False

    # Проверка длины
    if len(year) != 4:
        open_incorrect_year("Ошибка: год должен содержать ровно 4 цифры")
        return False

    # Преобразование в целое число
    try:
        year_int = int(year)
    except ValueError:
        open_incorrect_year("Ошибка: не удалось преобразовать год в число")
        return False

    # Проверка диапазона
    if year_int < 2016 or year_int > 2026:
        open_incorrect_year(
            f"Ошибка: год {year} выходит за допустимый диапазон (2016-2026)"
        )
        return False

    return True
