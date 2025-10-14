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
from sqlalchemy.orm import Session, relationship, validates
from pydantic import ValidationError
from typing import List

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
        day_worked (Optional[int]): количество отработанных дневных часов
            или None, если информация отсутствует.
        night_worked (Optional[int]): количество отработанных ночных часов
            или None, если информация отсутствует.
        employee (Employee): объект сотрудника, связанный через отношение ORM.
        calendar_day (CalendarDay): объект календарного дня, связанный через
            отношение ORM.
    """

    employee_id = Column(Integer, ForeignKey('employee.id'))
    calendar_day_id = Column(Integer, ForeignKey('calendarday.id'))

    day_worked = Column(Integer, nullable=True)
    night_worked = Column(Integer, nullable=True)

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
        if value is None:
            return value
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
        """
        Выполняет комплексную валидацию объекта, проверяя корректность
        заполненных данных.

        Основные проверки:
        - Валидация суммарного рабочего времени (дневное + ночное), если
            имеется отработанное дневное и ночное время.
        - Проверяет, что общее количество часов не превышает 24 в сутки

        При обнаружении нарушений выбрасывает исключение ValidationError
        с соответствующим сообщением об ошибке.
        """
        if (
            self.day_worked
            and self.night_worked
            and (self.day_worked + self.night_worked) > 24
        ):
            raise ValidationError(
                "Сумма отработанных часов не может превышать 24."
            )


class Table:
    """
    Класс для получения данных табеля сотрудников определенного отдела
    за определенный период.

    Отвечает за инициализацию и получение данных сотрудников и календарных дней
    для указанного отдела, года и месяца. Класс предоставляет методы для работы
    с данными табеля, включая получение списка сотрудников отдела, календарных
    дней и рабочих дней конкретных сотрудников.

    Основные возможности:
    * Получение списка сотрудников отдела
    * Получение календарных дней за указанный период
    * Получение рабочих дней конкретного сотрудника
    """

    def __init__(
            self, session: Session, year: str, month: str, department: str
    ):
        """
        Инициализирует объект Table.

        Параметры:
        session (Session): объект сессии базы данных для выполнения запросов
        year (str): год в строковом формате
        month (str): месяц в строковом формате
        department (str): название отдела

        Атрибуты класса:
        self.session (Session): сохраненная сессия базы данных
        self.year (str): сохраненный год
        self.month (str): сохраненный месяц
        self.department (str): сохраненное название отдела
        """

        self.session = session
        self.year = year
        self.month = month
        self.department = department

    def employees(self) -> List[Employee]:
        """
        Возвращает список сотрудников указанного отдела.

        Метод выполняет запрос к базе данных для получения всех сотрудников,
        принадлежащих к заданному отделу. Используется фильтрация по полю
        department модели Employee.

        Returns:
            List[Employee]: список объектов Employee, соответствующих фильтру
                по отделу
        """

        return self.session.query(Employee).filter(
            Employee.department == self.department
        ).all()

    def calendar_days(self) -> List[CalendarDay]:
        """
        Возвращает список календарных дней для указанного месяца и года.

        Метод выполняет запрос к базе данных для получения всех календарных
        дней, соответствующих указанным году и месяцу. При этом:
        * год преобразуется из строкового формата в целочисленный
        * месяц используется в исходном строковом формате

        Returns:
            List[CalendarDay]: список объектов CalendarDay, соответствующих
            указанным параметрам года и месяца
        """

        return self.session.query(CalendarDay).filter(
            CalendarDay.year == int(self.year),
            CalendarDay.month == self.month
        ).all()

    def get_work_days(self, employee: Employee) -> List[WorkDay]:
        """
        Возвращает список рабочих дней для указанного сотрудника за заданный
        период.

        Метод получает все рабочие дни сотрудника, которые попадают в указанный
        период (год и месяц). Сначала извлекаются все календарные дни за
        период, затем по их ID фильтруются рабочие дни конкретного сотрудника.

        Параметры:
        employee (Employee): объект сотрудника, для которого нужно получить
            рабочие дни

        Возвращает:
        List[WorkDay]: список объектов WorkDay, соответствующих указанному
            сотруднику и периоду
        """

        calendar_days = self.calendar_days()
        calendar_day_ids = [day.id for day in calendar_days]

        return self.session.query(WorkDay).filter(
            WorkDay.employee_id == employee.id,
            WorkDay.calendar_day_id.in_(calendar_day_ids)
        ).all()
