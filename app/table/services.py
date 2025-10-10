"""
Модуль размещения логики операций с объектами типа WorkDay.
"""

from typing import Optional

from .models import WorkDay


class WorkDayService:
    """
    Сервис для работы с рабочими днями сотрудников.
    Отвечает за создание и управление записями о рабочем времени сотрудников.
    """

    def create_work_day(
        employee_id: int,
        calendar_day_id: int,
        day_worked: Optional[int] = None,
        night_worked: Optional[int] = None
    ) -> WorkDay:
        """
        Создает новую запись о рабочем дне сотрудника.

        Параметры:
        employee_id (int): ID сотрудника, для которого создается запись
        calendar_day_id (int): ID календарного дня
        day_worked (Optional[int]): Количество отработанных дневных часов
        night_worked (Optional[int]): Количество отработанных ночных часов

        Возвращает:
        WorkDay: Созданный объект записи рабочего дня

        Примечание:
        Поля day_worked и night_worked являются опциональными и могут быть
        установлены позже, если информация о рабочем времени становится
        доступной позднее.
        """
        new_work_day = WorkDay(
            employee_id=employee_id,
            calendar_day_id=calendar_day_id,
            day_worked=day_worked,
            night_worked=night_worked
        )

        return new_work_day
