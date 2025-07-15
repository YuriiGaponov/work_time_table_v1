import tkinter as tk

from .base import BaseView
from ..commands import get_calendar
from .config import view_config


class MainView(BaseView):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.root.title(view_config.MAIN_VIEW_TITLE)
        self.root_lable.config(text=view_config.MAIN_VIEW_LABLE)

        # Кнопка запуска парсера производственного календаря
        self.get_calendar_button = tk.Button(
            self.root_content_frame,
            text=view_config.GET_CALENDAR_BUTTON_TEXT,
            command=get_calendar  # позже будет вызов окна выбора года
        )
        self.get_calendar_button.pack()
