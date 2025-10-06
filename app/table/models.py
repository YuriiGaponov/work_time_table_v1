"""
Модуль работы с записями о рабочих днях сотрудников.

Данный модуль реализует модель `WorkDay` — связующее звено
между сотрудниками (`Employee`) и календарными днями
(`CalendarDay`). Задача — хранить данные об отработанных
дневных/ночных часах для каждого сотрудника в конкретный
день.

Структура модуля:
* Модель `WorkDay` (наследник `Base`).
* Валидаторы данных.
* Конструктор с предварительной валидацией.

Ключевые особенности:
* **Уникальность записей.** Запрет на дублирование пары
  «сотрудник — календарный день» (`UniqueConstraint`).
* **Валидация часов.** Проверка на целое число, неотрицательность,
  максимум 24 часа.
* **Валидация ID.** Поля `employee_id`, `calendar_day_id` —
  положительные целые числа.
* **Суммарная проверка.** Сумма дневных и ночных часов ≤ 24.

Используемые зависимости:
* `SQLAlchemy` — работа с БД и ORM.
* `Pydantic` — обработка ошибок валидации.
* Модели: `Employee` (`app.employees`), `CalendarDay`
  (`app.calendar`), `Base` (`app.db`).

Пример использования:

from app.workdays import WorkDay

workday = WorkDay(
    employee_id=1,
    calendar_day_id=365,
    day_worked=8,
    night_worked=0
)

employee = workday.employee
calendar_day = workday.calendar_day
"""


from sqlalchemy import (
    Column, ForeignKey, Integer, UniqueConstraint
)
from sqlalchemy.orm import relationship, validates
from pydantic import ValidationError

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

    @validates('day_worked', 'night_worked')
    def validate_work_hours(self, key, value):
        """Валидация количества отработанных часов."""
        if not isinstance(value, int):
            raise ValidationError(f"Значение {key} должно быть целым числом.")
        if value < 0:
            raise ValidationError(
                f"Значение {key} не может быть отрицательным."
            )
        if value > 24:
            raise ValidationError(
                f"Значение {key} не может превышать 24 часа."
            )
        return value

    @validates('employee_id', 'calendar_day_id')
    def validate_ids(self, key, value):
        """Валидация ID-полей."""
        if not isinstance(value, int):
            raise ValidationError(f"Значение {key} должно быть целым числом.")
        if value <= 0:
            raise ValidationError(f"Значение {key} должно быть положительным.")
        return value

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

        # Вызываем валидацию при инициализации
        self._validate()

    def _validate(self):
        """Комплексная валидация объекта."""
        # Проверяем суммарное время работы за день
        if (self.day_worked + self.night_worked) > 24:
            raise ValidationError(
                "Сумма отработанных часов не может превышать 24."
            )
