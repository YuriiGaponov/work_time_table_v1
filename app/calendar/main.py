from typing import List, Tuple

from .models import CalendarDay


def save_calendar(
        session,
        downloaded_calendar: List[Tuple[int, int, str, int, bool]]
):
    """
    Сохраняет в БД сведения о днях года, полученные в ходе парсинга календаря,
    как объекты класса CalendarDay.
    """
    for calendar_day in downloaded_calendar:
        number, day, month, year, is_weekend = calendar_day
        if not session.query(CalendarDay).filter_by(
                number=number,
                day=day,
                month=month,
                year=year,
                is_weekend=is_weekend
             ).first():
            session.add(
                CalendarDay(
                    number=number,
                    day=day,
                    month=month,
                    year=year,
                    is_weekend=is_weekend
                )
            )
    session.commit()
