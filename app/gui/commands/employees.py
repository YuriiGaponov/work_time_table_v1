"""
Команды взаимодействия графического интерфейса с модулем работы с сотрудниками.
"""

from app.db import session
from app.employees import (
    EmployeeSchema,
    employee_exist,
    save_employee,
    validate_employee
)
from app.gui.views import BaseView


def open_validation_error(top_view: BaseView, message: str) -> None:
    """Открыть окно с сообщением об ошибке валидаци данных сотрудника."""
    from app.gui.views.employees_views import EmployeeExistView
    view = EmployeeExistView(top_view)
    view.root_head_lable.config(text=message)
    view.run()


def create_employee(top_view: BaseView, data: EmployeeSchema) -> None:
    """Создать сотрудника и добавить в БД."""
    # Проверка существования сотрудника
    if employee_exist(session, data):
        open_validation_error(
            top_view,
            'Сотрудник с такими данными уже существует!'
        )
    else:
        try:
            # Валидация введенных данных сотрудника
            validate_employee(data)  # временно отключена для дебага.
            save_employee(session, data)
        except ValueError as ve:
            open_validation_error(top_view, ve)
