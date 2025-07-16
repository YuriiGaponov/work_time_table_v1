import tkinter as tk

from .base import BaseView
from ..commands import open_year_selector
from .config import MainViewConfig


class MainView(BaseView):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.root.title(MainViewConfig.TITLE)
        self.root_lable.config(text=MainViewConfig.HEAD_LABLE)

        # Кнопка запуска парсера производственного календаря
        self.get_calendar_button = tk.Button(
            self.root_content_frame,
            text=MainViewConfig.GET_CALENDAR_BUTTON_TEXT,
            command=open_year_selector
        )
        self.get_calendar_button.pack()
