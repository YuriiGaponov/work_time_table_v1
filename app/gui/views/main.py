import tkinter as tk

from app.gui.commands import open_year_selector
from .base import BaseView
from .config import MainViewConfig as Config


class MainView(BaseView):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.root.title(Config.TITLE)
        self.root_head_lable.config(text=Config.HEAD_LABLE)

        # Кнопка запуска парсера производственного календаря
        self.get_calendar_button = tk.Button(
            self.root_content_frame,
            text=Config.GET_CALENDAR_BUTTON_TEXT,
            # command=open_year_selector
            command=self.year_selector
        )
        self.get_calendar_button.grid(row=0, column=0, sticky=Config.STICKY)

    def year_selector(self):
        """Открыть окно ввода года."""
        open_year_selector(self)
