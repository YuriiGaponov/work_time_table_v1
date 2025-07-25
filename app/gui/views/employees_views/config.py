from app.gui.views.base import BaseConfig


class EmployeeManagerViewConfig(BaseConfig):
    """Настройки окна работы со списком сотрудников."""

    TITLE: str = 'Список сотрудников'
    HEAD_LABLE: str = 'Список сотрудников'
    ADD_EMPLOYEE_BUTTON_TEXT: str = 'Добавить сотрудника'


class CreateEmployeeBaseViewConfig(BaseConfig):
    """Настройки окна создания нового сотрудника."""

    TITLE: str = 'Добавление сотрудника'
    HEAD_LABLE: str = 'Введите фамилию, имя, отчество (при наличии), отдел'
