"""
Модуль окон интерфеса для CRUD операций с сотрудниками
поиска данных сотрудников в БД.
"""

from app.db import session
from app.gui.commands import (
    create_employee,
    search_employees
)
from app.gui.views.base import BaseListView
from app.gui.commands import open_search_view
from .config import (
    CreateEmployeeViewConfig,
    SearchEmployeeViewConfig,
    ShowEmployeeListViewConfig
)
from .crud_base_employee import CRUDEmployeeBaseView
from .validation_error import EmployeeErrorView


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
        open_search_view(
            self,
            ShowEmployeeListView,
            search_employees(session, super().confirm())
        )


class ShowEmployeeListView(BaseListView):
    """Окно отображения списка сотрудников."""

    def __init__(self, top_view, items=None):
        """Инициализация окна."""
        super().__init__(top_view, items)
        self.root.title(ShowEmployeeListViewConfig.TITLE)
        self.root_head_lable.config(
            text=ShowEmployeeListViewConfig.HEAD_LABLE
        )
        self.tree.config(
            columns=ShowEmployeeListViewConfig.TREE_COLUMNS,
            show=ShowEmployeeListViewConfig.TREE_SHOW
        )

        ShowEmployeeListViewConfig.configure_tree(self.tree)
        ShowEmployeeListViewConfig.add_employees(self.tree, self.items)


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
        create_employee(
            self,
            super().confirm(),
            EmployeeErrorView
        )
