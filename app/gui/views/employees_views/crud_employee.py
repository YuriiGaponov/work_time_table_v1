import tkinter as tk

from app.gui.views.base import BaseModalView
from .config import CreateEmployeeBaseViewConfig


class CRUDEmployeeBaseView(BaseModalView):
    """Шаблон создания окон для CRUD операций с сотрудниками."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)

        self.name_entry_label = tk.Label(
            self.root_content_frame
        )


class CreateEmployeeBaseView(CRUDEmployeeBaseView):
    """Окно создания нового сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(CreateEmployeeBaseViewConfig.TITLE)
        self.root_head_lable.config(
            text=CreateEmployeeBaseViewConfig.HEAD_LABLE
        )
