import tkinter as tk

from app.gui.commands import (
    get_calendar, not_validate_year, open_incorrect_year
)
from app.gui.views.base import BaseModalView
from .config import YearSelectorViewConfig


class YearSelectorView(BaseModalView):
    """Окно выбора года для парсинга календаря."""

    def __init__(self, top_view):
        super().__init__(top_view)
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
        validation = not_validate_year(year)
        if validation:
            open_incorrect_year(validation, self)
        else:
            get_calendar(year)
            self.root.destroy()

    def clean(self):
        """Очищает поле ввода года."""
        self.select_year_entry.delete(0, tk.END)
