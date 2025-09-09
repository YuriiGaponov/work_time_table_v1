"""
Модуль окон интерфеса для взаимодействия с пакетом
обработки табелей.
"""

import tkinter as tk
from tkinter import ttk

from app.gui.commands import open_modal_view
from app.gui.views.base import BaseListView, BaseModalView, base_grid
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
            self.root_content_frame,
            text=TableSelectorViewConfig.OPEN_TABLE_BUTTON_TEXT,
            command=self.open_table
        )
        # Кнопка очистки полей.
        self.clean_button = ttk.Button(
            self.root_content_frame,
            text=TableSelectorViewConfig.CLEAN_BUTTON_TEXT,
            command=self.clean
        )

        # Расположение виджетов.
        base_grid(self.year_entry_label, 0, 0, TableSelectorViewConfig)
        base_grid(self.year_entry, 0, 1, TableSelectorViewConfig)
        base_grid(self.month_entry_label, 1, 0, TableSelectorViewConfig)
        base_grid(self.month_entry, 1, 1, TableSelectorViewConfig)
        base_grid(self.department_entry_label, 2, 0, TableSelectorViewConfig)
        base_grid(self.department_entry, 2, 1, TableSelectorViewConfig)
        base_grid(self.open_tale_button, 3, 0, TableSelectorViewConfig)
        base_grid(self.clean_button, 3, 1, TableSelectorViewConfig)

    def open_table(self):
        """Открывает табель с выбранными параметрами."""
        open_modal_view(self, TableView)

    def clean(self):
        """Очищает заполненные поля выбора параметров."""
        self.year_entry.delete(0, tk.END)
        self.month_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)


class TableView(BaseListView):
    """Окно отображения табеля."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(TableViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableViewConfig.HEAD_LABLE
        )
