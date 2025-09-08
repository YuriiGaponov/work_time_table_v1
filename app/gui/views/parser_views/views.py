import tkinter as tk
from tkinter import ttk

from app.gui.commands import (
    get_calendar,
    not_validate_year
)
from app.gui.commands import open_info_view
from app.gui.views.base import BaseModalView, BaseErrorView
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

        self.select_year_lable.grid(
            row=0,
            column=0,
            sticky=YearSelectorViewConfig.STICKY
        )
        self.select_year_entry.grid(
            row=0,
            column=1,
            sticky=YearSelectorViewConfig.STICKY
        )
        self.confirm_button.grid(
            row=1,
            column=0,
            sticky=YearSelectorViewConfig.STICKY
        )
        self.clean_button.grid(
            row=1,
            column=1,
            sticky=YearSelectorViewConfig.STICKY
        )

    def confirm(self):
        """Получает год из поля ввода и передает его в парсер."""
        year = self.select_year_entry.get()
        validation = not_validate_year(year)
        if validation:
            open_info_view(validation, self, IncorrectYearView)
        else:
            get_calendar(year)
            self.root.destroy()

    def clean(self):
        """Очищает поле ввода года."""
        self.select_year_entry.delete(0, tk.END)


class IncorrectYearView(BaseErrorView):
    """Информационное окно с сообщение о неверном вводе года."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(IncorrectYearViewConfig.TITLE)
