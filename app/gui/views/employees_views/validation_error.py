"""
Модуль окон интерфейса для вывода данных об ошибках,
возникающих при обработке данных сотрудников.
"""

from app.gui.views.base import BaseErrorView
from .config import EmployeeErrorViewConfig


class EmployeeErrorView(BaseErrorView):
    """
    Информационное окно с сообщением об ошибке
    создания сотрудника с вводимыми данными.
    """

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(EmployeeErrorViewConfig.TITLE)
