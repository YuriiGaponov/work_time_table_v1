import tkinter as tk

from ..commands import get_calendar, validate_year
from .base import BaseView, BaseErrorView
from .config import IncorrectYearViewConfig, YearSelectorViewConfig


class YearSelectorView(BaseView):
    """Окно выбора года для парсинга календаря."""

    def __init__(self):
        super().__init__()
        self.root.title(YearSelectorViewConfig.TITLE)
        self.root_head_lable.config(text=YearSelectorViewConfig.HEAD_LABLE)

        self.select_year_lable = tk.Label(
            self.root_content_frame,
            text=YearSelectorViewConfig.CONTENT_LABLE
        )
        self.select_year_entry = tk.Entry(self.root_content_frame)
        self.confirm_button = tk.Button(
            self.root_content_frame,
            text=YearSelectorViewConfig.CONFIRM_BUTTON_TEXT,
            command=self.confirm
        )
        self.clean_button = tk.Button(
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
        if validate_year(year):
            get_calendar(year)
            self.root.destroy()

    def clean(self):
        """Очищает поле ввода года."""
        self.select_year_entry.delete(0, tk.END)


class IncorrectYearView(BaseErrorView):
    """Информационное окно с сообщение о неверном вводе года."""

    def __init__(self):
        super().__init__()
        self.root_head_lable.config(text=IncorrectYearViewConfig.HEAD_LABLE)
