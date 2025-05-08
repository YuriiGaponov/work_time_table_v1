from .models import CalendarDay


def save_calendar(session, downloaded_calendar: list):
    """
    Сохраняет в БД сведения о днях года, полученные в ходе парсинга календаря,
    как объекты класса CalendarDay.
    """
    for day_in_calendar in downloaded_calendar:
        number, day, month, year, is_weekend = day_in_calendar
        calendar_day = CalendarDay(
            number=number,
            day=day,
            month=month,
            year=year,
            is_weekend=is_weekend
        )

        session.add(calendar_day)

    session.commit()
