"""
Модуль работы с сущностью «Рабочий день» (WorkDay).

Модуль реализует модель данных для учёта отработанного времени сотрудников,
представляющую собой связующее звено между сотрудниками и календарными днями.

Основные функции модуля:
    * хранение информации о количестве отработанных дневных и ночных часов;
    * обеспечение связи между таблицами сотрудников (Employee) и календарных
    дней (CalendarDay);
    * предоставление структуры для учёта рабочего времени в рамках системы.

Используемые внешние зависимости:
    * SQLAlchemy — для построения ORM-модели;
    * app.calendar.CalendarDay — сущность календарного дня;
    * app.db.Base — базовый класс для моделей SQLAlchemy;
    * app.employees.Employee — сущность сотрудника.

Ключевые компоненты модуля:
    * класс `WorkDay` — основная модель, описывающая рабочий день сотрудника.

Типичное использование:
    1. Создание записи о рабочем дне:
        ```python
        work_day = WorkDay(
            employee_id=1,
            calendar_day_id=42,
            day_worked=8,
            night_worked=2
        )
        ```
    2. Доступ к связанным данным:
        ```python
        # Получение сотрудника по записи рабочего дня
        employee = work_day.employee

        # Получение календарного дня по записи рабочего дня
        calendar_day = work_day.calendar_day
        ```
"""

from sqlalchemy import (
    Column, ForeignKey, Integer, UniqueConstraint
)
from sqlalchemy.orm import relationship

from app.calendar import CalendarDay
from app.db import Base
from app.employees import Employee


class WorkDay(Base):
    """
    Класс для хранения информации о рабочем дне сотрудника.

    Представляет собой связующую сущность между сотрудниками и календарными
    днями, хранящую данные о количестве отработанных дневных и ночных часов.

    Атрибуты класса:
        employee_id (int): идентификатор сотрудника, связанный с записью.
        calendar_day_id (int): идентификатор календарного дня, к которому
            относится запись рабочего дня.
        day_worked (int): количество отработанных дневных часов.
        night_worked (int): количество отработанных ночных часов.
        employee (Employee): объект сотрудника, связанный через отношение ORM.
        calendar_day (CalendarDay): объект календарного дня, связанный через
            отношение ORM.
    """

    employee_id = Column(Integer, ForeignKey('employee.id'))
    calendar_day_id = Column(Integer, ForeignKey('calendarday.id'))

    day_worked = Column(Integer)
    night_worked = Column(Integer)

    employee = relationship(
        Employee,
        back_populates='work_days'
    )
    calendar_day = relationship(
        CalendarDay,
        back_populates='work_days'
    )

    __table_args__ = (
        UniqueConstraint('employee_id', 'calendar_day_id',
                         name='uix_employee_calendar_day'),
    )

    def __init__(self,
                 employee_id: int,
                 calendar_day_id: int,
                 day_worked: int = 0,
                 night_worked: int = 0):
        """
        Инициализация объекта рабочего дня.

        :param employee_id: ID сотрудника
        :param calendar_day_id: ID календарного дня
        :param day_worked: количество отработанных дневных часов
        :param night_worked: количество отработанных ночных часов
        """
        self.employee_id = employee_id
        self.calendar_day_id = calendar_day_id
        self.day_worked = day_worked
        self.night_worked = night_worked
