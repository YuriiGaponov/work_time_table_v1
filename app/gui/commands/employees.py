"""
Команды взаимодействия графического интерфейса с модулем работы с сотрудниками.
"""

from pydantic import ValidationError
from typing import Callable

from app.db import session
from app.employees import (
    EmployeeSchema,
    employee_exist,
    save_employee,
    validate_employee
)
from app.gui.views.config import ErrorMessage
from app.gui.views import BaseView
from .views import open_info_view


def create_employee(
        top_view: BaseView,
        data: EmployeeSchema,
        ErrorViewClass: Callable
) -> None:
    """
    Создать сотрудника и добавить в БД.
    При возникновении ошибок открыть окно с сообщением об ошибке.
    """
    # Проверка существования сотрудника
    if employee_exist(session, data):
        open_info_view(top_view, ErrorViewClass, ErrorMessage.EMPLOYEE_EXIST)
    else:
        try:
            # Валидация введенных данных сотрудника
            validate_employee(data)
            save_employee(session, data)
        except (ValueError, ValidationError) as e:
            if isinstance(e, ValidationError):
                # Извлекаем все сообщения об ошибках
                errors = e.errors()
                error_messages = [error['msg'] for error in errors]
                # Формируем объединенное сообщение
                message = '\n'.join(error_messages)
            else:
                args = e.args
                message = args[0] if args else "Неизвестная ошибка"

            open_info_view(top_view, ErrorViewClass, message)
