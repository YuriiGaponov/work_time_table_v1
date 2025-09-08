from tkinter import ttk

from app.gui.commands import open_modal_view
from .base import BaseView
from .config import MainViewConfig as Config
from .employees_views import EmployeeManagerView
from .parser_views import YearSelectorView
from .table_views import TableSelectorView


class MainView(BaseView):
    """Главное окно приложения."""

    def __init__(self):
        super().__init__()
        self.root.title(Config.TITLE)
        self.root_head_lable.config(text=Config.HEAD_LABLE)

        # Кнопка запуска парсера производственного календаря
        self.get_calendar_button = ttk.Button(
            self.root_content_frame,
            text=Config.GET_CALENDAR_BUTTON_TEXT,
            command=self.year_selector
        )

        # Кнопка запуска парсера производственного календаря
        self.employees_button = ttk.Button(
            self.root_content_frame,
            text=Config.EMPLOYEES_BUTTON_TEXT,
            command=self.employee_manager
        )

        # Кнопка отображения табеля
        self.table_button = ttk.Button(
            self.root_content_frame,
            text=Config.TABLE_BUTTON_TEXT,
            command=self.table_manager
        )

        self.get_calendar_button.grid(row=0, column=0, sticky=Config.STICKY)
        self.employees_button.grid(row=0, column=1, sticky=Config.STICKY)
        self.table_button.grid(row=0, column=2, sticky=Config.STICKY)

    def year_selector(self):
        """Открыть окно ввода года."""
        open_modal_view(self, YearSelectorView)

    def employee_manager(self):
        """Открыть окно управления данными сотрудников."""
        open_modal_view(self, EmployeeManagerView)

    def table_manager(self):
        """Открыть окно управления табелями."""
        open_modal_view(self, TableSelectorView)
