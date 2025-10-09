"""
Бизнес-логика построения табеля.

Табель включает в себя сотрудников одного отдела (столбцы),
дни месяца (колонки), в ячейках находятся значения для количества часов,
отработанных сотрудников в дневное и ночное время.

Табель создается для каждого дня года и каждого сотрудника при создании нового
сотрудника или при скачивании календаря за год, при условии,
что такого табеля еще нет в БД.
"""

from typing import List

from app.calendar import CalendarDay
from app.db import session
from app.employees import Employee
from app.table import WorkDay, WorkDayService


# При сохранении года календаря:
def create_table_for_downloaded_calendar(year: str):
    """
    Создает табели для всех дней года скачанного календаря
    для всех сотрудников в БД.
    """

    # - получить всех существующих сотрудников
    employees: List[Employee] = session.query(Employee).all()
    # если список employees пуст, выполнение функции прекращается
    if not employees:
        pass

    # - получить все дни по номеру года (год получить из поля парсера)
    calendar_days: List[CalendarDay] = session.query(
        CalendarDay
    ).filter(CalendarDay.year == int(year)).all()

    if not calendar_days:
        pass

    # - пройти циклом по списку сотрудников, для каждого сотрудника создать
    # WorkDay, если он нес существует (написать провеку)
    for employee in employees:
        for calendar_day in calendar_days:
            workday = WorkDay(employee_id=employee.id, calendar_day_id=calendar_day.id)
            session.add(workday)
    session.commit()
