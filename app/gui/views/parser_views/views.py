"""
Модуль окон интерфейса интерфейса для
взаимодействия с модулем парсинга.
"""

import tkinter as tk
from tkinter import ttk

from app.gui.commands import (
    get_calendar,
    not_validate_year,
    open_info_view
)
from app.gui.views.base import BaseModalView, BaseErrorView, base_grid
from app.srvices import create_table_for_downloaded_calendar
from .config import IncorrectYearViewConfig, YearSelectorViewConfig


class YearSelectorView(BaseModalView):
    """Окно выбора года для парсинга календаря."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(YearSelectorViewConfig.TITLE)
        self.root_head_lable.config(text=YearSelectorViewConfig.HEAD_LABLE)

        self.select_year_lable = ttk.Label(
            self.root_content_frame,
            text=YearSelectorViewConfig.CONTENT_LABLE
        )
        self.select_year_entry = ttk.Entry(self.root_content_frame)
        self.confirm_button = ttk.Button(
            self.root_content_frame,
            text=YearSelectorViewConfig.CONFIRM_BUTTON_TEXT,
            command=self.confirm
        )
        self.clean_button = ttk.Button(
            self.root_content_frame,
            text=YearSelectorViewConfig.CLEAN_BUTTON_TEXT,
            command=self.clean
        )

        # Расположение виджетов.
        base_grid(self.select_year_lable, 0, 0, YearSelectorViewConfig)
        base_grid(self.select_year_entry, 0, 1, YearSelectorViewConfig)
        base_grid(self.confirm_button, 1, 0, YearSelectorViewConfig)
        base_grid(self.clean_button, 1, 1, YearSelectorViewConfig)

    def confirm(self):
        """Получает год из поля ввода и передает его в парсер."""
        year = self.select_year_entry.get()
        validation = not_validate_year(year)
        if validation:
            open_info_view(self, IncorrectYearView, validation)
        else:
            get_calendar(year)
            create_table_for_downloaded_calendar(year)
            self.root.destroy()

    def clean(self):
        """Очищает поле ввода года."""
        self.select_year_entry.delete(0, tk.END)


class IncorrectYearView(BaseErrorView):
    """Информационное окно с сообщение о неверном вводе года."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(IncorrectYearViewConfig.TITLE)
