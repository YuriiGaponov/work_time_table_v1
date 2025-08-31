from app.gui.views.base import BaseErrorView
from .config import EmployeeExistViewConfig


class EmployeeExistView(BaseErrorView):
    """
    Информационное окно с сообщение о существовании сотрудника
    с вводимыми данными.
    """

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(EmployeeExistViewConfig.TITLE)
