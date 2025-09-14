from app.core import app_settings


def not_validate_year(year: str) -> bool:
    """Валидирует значение, переданное в поле года."""
    if not year:
        return 'Ошибка: год не может быть пустым'

    # Проверка на наличие только цифр
    if not year.isdigit():
        return 'Ошибка: год должен содержать только цифры'

    # Проверка длины
    if len(year) != 4:
        return 'Ошибка: год должен содержать ровно 4 цифры'

    # Преобразование в целое число
    try:
        year_int = int(year)
    except ValueError:
        return 'Ошибка: не удалось преобразовать год в число'

    # Проверка диапазона
    if not (
        app_settings.MIN_PARSE_YEAR <= year_int <= app_settings.MAX_PARSE_YEAR
    ):
        return (
            f'Ошибка: год {year} выходит за допустимый диапазон '
            f'({app_settings.MIN_PARSE_YEAR}-{app_settings.MAX_PARSE_YEAR})'
        )

    return False
