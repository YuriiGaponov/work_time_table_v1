"""
Модуль размещения логики операций с объектами типа WorkDay.
"""

from sqlalchemy.orm import Session
from .models import WorkDay


class WorkDayService:
    """
    Сервис для работы с рабочими днями сотрудников.
    Отвечает за создание и управление записями о рабочем времени сотрудников.
    """

    # def __init__(self, session: Session):
    #     """
    #     Инициализирует сервис с заданной сессией SQLAlchemy.

    #     :param session: сессия SQLAlchemy для взаимодействия с базой данных.
    #     """
    #     self.session = session

    def create_work_day(
        # self,
        employee_id: int,
        calendar_day_id: int,
        day_worked: int = 0,
        night_worked: int = 0
    ) -> WorkDay:
        """
        Создаёт новую запись о рабочем дне сотрудника.

        :param employee_id: ID сотрудника, для которого создаётся запись.
        :param calendar_day_id: ID календарного дня, к которому относится
            запись.
        :param day_worked: количество отработанных дневных часов
            (по умолчанию — 0).
        :param night_worked: количество отработанных ночных часов
            (по умолчанию — 0).
        :return: объект `WorkDay`, представляющий созданную запись.
        :raises: исключения, связанные с операциями с базой данных
            (например, `IntegrityError` при нарушении ограничений БД).
        """
        new_work_day = WorkDay(
            employee_id=employee_id,
            calendar_day_id=calendar_day_id,
            day_worked=day_worked,
            night_worked=night_worked
        )
        # self.session.add(new_work_day)
        # self.session.commit()
        return new_work_day
