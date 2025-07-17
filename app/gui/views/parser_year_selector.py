import tkinter as tk

from ..commands import get_calendar
from .base import BaseView
from .config import ParserYearSelectorViewConfig as Config


class ParserYearSelector(BaseView):
    """Окно выбора года для парсинга календаря."""

    def __init__(self):
        super().__init__()
        self.root.title(Config.TITLE)
        self.root_lable.config(text=Config.HEAD_LABLE)

        self.select_year_lable = tk.Label(
            self.root_content_frame,
            text=Config.CONTENT_LABLE
        )
        self.select_year_entry = tk.Entry(self.root_content_frame)
        self.confirm_button = tk.Button(
            self.root_content_frame,
            text=Config.CONFIRM_BUTTON_TEXT,
            command=self.confirm
        )
        self.clean_button = tk.Button(
            self.root_content_frame,
            text=Config.CLEAN_BUTTON_TEXT,
            command=self.clean
        )

        self.select_year_lable.grid(row=0, column=0, sticky=Config.STICKY)
        self.select_year_entry.grid(row=0, column=1, sticky=Config.STICKY)
        self.confirm_button.grid(row=1, column=0, sticky=Config.STICKY)
        self.clean_button.grid(row=1, column=1, sticky=Config.STICKY)

    def confirm(self):
        """Получает год из поля ввода и передает его в парсер."""
        get_calendar(self.select_year_entry.get())
        self.root.destroy()

    def clean(self):
        """Очищает поле ввода года."""
        self.select_year_entry.delete(0, tk.END)
