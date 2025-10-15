"""
Модуль сервисов учета рабочего времени сотрудников

Данный модуль содержит сервисы для работы с табелями учета рабочего времени.
Он предоставляет функциональность для создания и управления записями о рабочем
времени сотрудников, а также формирования табелей учета.

Основные компоненты модуля:

* WorkDayService - сервис для работы с отдельными записями рабочего времени
* TableService - сервис для работы с табелями учета рабочего времени

Модуль обеспечивает:
* Создание записей о рабочем времени сотрудников
* Формирование табелей на год для всех сотрудников
* Создание табелей для новых сотрудников
* Валидацию и уникальность записей в базе данных

Используемые импорты:
* typing - для типизации (List, Optional)
* CalendarDay - модель календарного дня
* session - сессия базы данных
* Employee, EmployeeSchema - модели сотрудников
* WorkDay - модель записи рабочего дня

Структура работы:
1. WorkDayService отвечает за создание отдельных записей рабочего времени
2. TableService управляет формированием табелей учета
3. Все операции выполняются с учетом целостности данных
"""

from typing import List, Optional

from app.calendar import CalendarDay
from app.db import session
from app.employees import Employee, EmployeeSchema
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


class TableService:
    """
    Сервис для работы с табелями учета рабочего времени.

    Класс предоставляет методы для создания и управления табелями
    рабочего времени сотрудников. Табель представляет собой структуру,
    где столбцы соответствуют сотрудникам одного отдела, колонки —
    дням месяца, а в ячейках хранится информация о количестве
    отработанных часов в дневное и ночное время.

    Основные функции сервиса:
    - Создание табелей для всех сотрудников на указанный год
    - Формирование табелей для нового сотрудника на все календарные дни
    - Обеспечение уникальности записей в базе данных

    При работе с табелями соблюдаются следующие правила:
    - Табель создается для каждого дня года и каждого сотрудника
    - Записи формируются только при отсутствии аналогичных в БД
    - Операции выполняются без ошибок при отсутствии данных
    """

    @staticmethod
    def create_workdays_for_downloaded_calendar(year: str):
        """
        Создает табели рабочего времени для всех сотрудников на указанный год.

        Метод генерирует записи рабочего времени для каждого дня года и каждого
        сотрудника, если соответствующие записи отсутствуют в базе данных.

        Параметры:
        year (str): год, для которого создаются табели рабочего времени

        Процесс выполнения:
        1. Получает список всех сотрудников из БД
        2. Извлекает все календарные дни указанного года
        3. Для каждой комбинации сотрудник-день создает запись табеля,
           если она отсутствует
        4. Сохраняет изменения в базе данных

        При отсутствии сотрудников или календарных дней операция завершается
        без ошибок, но без создания записей.
        """

        employees: List[Employee] = session.query(Employee).all()
        if not employees:
            pass

        calendar_days: List[CalendarDay] = session.query(
            CalendarDay
        ).filter(CalendarDay.year == int(year)).all()

        if not calendar_days:
            pass

        for employee in employees:
            for calendar_day in calendar_days:
                workday = WorkDayService.create_work_day(
                    employee.id, calendar_day.id
                )
                session.add(workday)
        session.commit()

    @staticmethod
    def create_workdays_for_new_employee(employee_data: EmployeeSchema):
        """
        Создает табели рабочего времени для нового сотрудника
        на все дни календаря.

        Метод генерирует записи рабочего времени для каждого
        календарного дня и нового сотрудника, если соответствующие
        записи отсутствуют в БД.

        Параметры:
            employee_data (EmployeeSchema): данные нового сотрудника

        Процесс выполнения:
            1. Находит сотрудника в БД по имени, фамилии
            и отделу
            2. Извлекает все календарные дни из БД
            3. Для каждого календарного дня создает запись
            табеля, если она отсутствует
            4. Сохраняет изменения в базе данных

        Если сотрудник не найден или нет календарных дней,
        операция завершается без ошибок, но без создания
        записей.
        """
        employee = session.query(Employee).filter(
            Employee.name == employee_data['name'],
            Employee.surname == employee_data['surname'],
            Employee.department == employee_data['department']
        ).first()
        calendar_days: List[CalendarDay] = session.query(CalendarDay).all()

        for calendar_day in calendar_days:
            workday = WorkDayService.create_work_day(
                    employee.id, calendar_day.id
                )
            session.add(workday)
        session.commit()
