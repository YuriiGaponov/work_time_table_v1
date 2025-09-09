"""
Модуль окон интерфеса для взаимодействия с модулем
обработки табелей.
"""

from tkinter import ttk

from app.gui.views.base import BaseListView, BaseModalView
from .config import TableViewConfig, TableSelectorViewConfig


class TableSelectorView(BaseModalView):
    """Окно выбора параметров для отображения табеля."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)

        self.root.title(TableSelectorViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableSelectorViewConfig.HEAD_LABLE
        )
        # Год.
        self.year_entry_label = ttk.Label(
            self.root_content_frame,
            text=TableSelectorViewConfig.YEAR_ENTRY_LABEL_TEXT
        )
        self.year_entry = ttk.Entry(
            self.root_content_frame
        )
        # Месяц.
        self.month_entry_label = ttk.Label(
            self.root_content_frame,
            text=TableSelectorViewConfig.MONTH_ENTRY_LABEL_TEXT
        )
        self.month_entry = ttk.Entry(
            self.root_content_frame
        )
        # Отдел.
        self.department_entry_label = ttk.Label(
            self.root_content_frame,
            text=TableSelectorViewConfig.DEPARTMENT_ENTRY_LABEL_TEXT
        )
        self.department_entry = ttk.Entry(
            self.root_content_frame
        )
        # Кнопка открытия табеля.
        self.open_tale_button = ttk.Button(
            self.root_content_frame
        )
        # Кнопка очистки полей.
        self.clean_button = ttk.Button(
            self.root_content_frame
        )

        # Расположение виджетов.
        self.year_entry_label.grid(
            row=0, column=0,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.year_entry.grid(
            row=0, column=1,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.month_entry_label.grid(
            row=1, column=0,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.month_entry.grid(
            row=1, column=1,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.department_entry_label.grid(
            row=2, column=0,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.department_entry.grid(
            row=2, column=1,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.open_tale_button.grid(
            row=3, column=0,
            sticky=TableSelectorViewConfig.STICKY
        )
        self.clean_button.grid(
            row=3, column=1,
            sticky=TableSelectorViewConfig.STICKY
        )


class TableView(BaseListView):
    """Окно отображения табеля."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(TableViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableViewConfig.HEAD_LABLE
        )
