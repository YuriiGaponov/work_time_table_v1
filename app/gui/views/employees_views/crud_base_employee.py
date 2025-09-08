"""
Модуль базового окна интерфейса для CRUD операций с данными сотрудников,
используемого для наследования во вложенных модулях.
"""

import tkinter as tk
from tkinter import ttk

from app.employees import EmployeeSchema
from app.gui.views.base import BaseModalView
from .config import CRUDEmployeeBaseViewConfig


class CRUDEmployeeBaseView(BaseModalView):
    """
    Шаблон создания окон для CRUD операций с сотрудниками.
    Включает поля для ввода фамилии, имени, отчества, отдела.
    """

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)

        # Имя
        self.name_entry_label = ttk.Label(
            self.root_content_frame,
            text=CRUDEmployeeBaseViewConfig.NAME_ENTRY_LABLE_TEXT
        )
        self.name_entry = ttk.Entry(
            self.root_content_frame,
        )
        # Отчество
        self.patronymic_entry_label = ttk.Label(
            self.root_content_frame,
            text=CRUDEmployeeBaseViewConfig.PATRONYMIC_ENTRY_LABLE_TEXT
        )
        self.patronymic_entry = ttk.Entry(
            self.root_content_frame,
        )
        # Фамилия
        self.surname_entry_label = ttk.Label(
            self.root_content_frame,
            text=CRUDEmployeeBaseViewConfig.SURNAME_ENTRY_LABLE_TEXT
        )
        self.surname_entry = ttk.Entry(
            self.root_content_frame,
        )
        # Отдел
        self.department_entry_label = ttk.Label(
            self.root_content_frame,
            text=CRUDEmployeeBaseViewConfig.DEPARTMENT_ENTRY_LABLE_TEXT
        )
        self.department_entry = ttk.Entry(
            self.root_content_frame,
        )
        # Кнопка подтверждения
        self.confirm_button = ttk.Button(
            self.root_content_frame,
            command=self.confirm
        )
        # Кнопка очистки
        self.clean_button = ttk.Button(
            self.root_content_frame,
            text=CRUDEmployeeBaseViewConfig.CLEAN_BUTTON_TEXT,
            command=self.clean
        )

        self.name_entry_label.grid(
            row=0, column=0,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.name_entry.grid(
            row=0, column=1,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.patronymic_entry_label.grid(
            row=1, column=0,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.patronymic_entry.grid(
            row=1, column=1,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.surname_entry_label.grid(
            row=2, column=0,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.surname_entry.grid(
            row=2, column=1,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.department_entry_label.grid(
            row=3, column=0,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.department_entry.grid(
            row=3, column=1,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.confirm_button.grid(
            row=4, column=0,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )
        self.clean_button.grid(
            row=4, column=1,
            sticky=CRUDEmployeeBaseViewConfig.STICKY
        )

    def confirm(self) -> EmployeeSchema:
        """Возвращает значения заполненных полей."""
        return {
            'name': self.name_entry.get(),
            'patronymic': self.patronymic_entry.get(),
            'surname': self.surname_entry.get(),
            'department': self.department_entry.get()
        }

    def clean(self):
        """Очищает заполненные поля ввода."""
        self.name_entry.delete(0, tk.END)
        self.patronymic_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
