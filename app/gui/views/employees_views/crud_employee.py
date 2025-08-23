from app.gui.commands import create_employee, open_list_employee
from app.gui.views.base import BaseListView
from .config import (
    CreateEmployeeViewConfig,
    SearchEmployeeViewConfig,
    ShowEmployeeListViewConfig
)
from .crud_base_employee import CRUDEmployeeBaseView


class SearchEmployeeView(CRUDEmployeeBaseView):
    """Окно поиска сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(SearchEmployeeViewConfig.TITLE)
        self.root_head_lable.config(
            text=SearchEmployeeViewConfig.HEAD_LABLE
        )
        self.confirm_button.config(
            text=SearchEmployeeViewConfig.COMFIRM_BUTTON_TEXT
        )

    def confirm(self):
        """Найти сотрудника."""
        # return super().confirm()
        open_list_employee(self)


class ShowEmployeeListView(BaseListView):
    """Окно отображения списка сотрудников."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(ShowEmployeeListViewConfig.TITLE)
        self.root_head_lable.config(
            text=ShowEmployeeListViewConfig.HEAD_LABLE
        )


class CreateEmployeeView(CRUDEmployeeBaseView):
    """Окно создания нового сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(CreateEmployeeViewConfig.TITLE)
        self.root_head_lable.config(
            text=CreateEmployeeViewConfig.HEAD_LABLE
        )
        self.confirm_button.config(
            text=CreateEmployeeViewConfig.COMFIRM_BUTTON_TEXT
        )

    def confirm(self):
        """Создать сотрудника."""
        create_employee(self, super().confirm())
