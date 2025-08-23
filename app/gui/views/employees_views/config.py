from app.gui.views.base import BaseConfig


class EmployeeManagerViewConfig(BaseConfig):
    """Настройки окна работы со списком сотрудников."""

    TITLE: str = 'Список сотрудников'
    HEAD_LABLE: str = 'Список сотрудников'
    ADD_EMPLOYEE_BUTTON_TEXT: str = 'Добавить сотрудника'
    SEARCH_EMPLOYEE_BUTTON_TEXT: str = 'Найти сотрудника'


class CRUDEmployeeBaseViewConfig(BaseConfig):
    """Настройки окна создания нового сотрудника."""

    NAME_ENTRY_LABLE_TEXT: str = 'Имя'
    PATRONYMIC_ENTRY_LABLE_TEXT: str = 'Отчество'
    SURNAME_ENTRY_LABLE_TEXT: str = 'Фамилия'
    DEPARTMENT_ENTRY_LABLE_TEXT: str = 'Отдел'
    CLEAN_BUTTON_TEXT: str = 'Очистить'


class SearchEmployeeViewConfig(CRUDEmployeeBaseViewConfig):
    """Настройки окна поиска сотрудника."""

    TITLE: str = 'Найти сотрудника'
    HEAD_LABLE: str = 'Введите один или несколько параметров поиска'
    COMFIRM_BUTTON_TEXT: str = 'Найти'


class ShowEmployeeListViewConfig(BaseConfig):
    """Настройки окна отображения списка сотрудников."""

    TITLE: str = 'Список сотрудников'
    HEAD_LABLE: str = 'Результаты поиска сотрудников'


class CreateEmployeeViewConfig(CRUDEmployeeBaseViewConfig):
    """Настройки окна создания нового сотрудника."""

    TITLE: str = 'Добавление сотрудника'
    HEAD_LABLE: str = 'Введите фамилию, имя, отчество (при наличии), отдел'
    COMFIRM_BUTTON_TEXT: str = 'Добавить'


class EmployeeExistViewConfig(BaseConfig):
    """
    Настройки информационного окна с сообщением с сообщение о существовании
    сотрудника с вводимыми данными.
    """

    TITLE: str = 'Сотрудник уже существует.'
