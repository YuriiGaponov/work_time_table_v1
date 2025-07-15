import tkinter as tk


class BaseView():
    """Базовый класс окн приложения"""

    def __init__(self):
        """Инициализация окна"""
        self.root = tk.Tk()

    def run(self):
        """Запуск окна."""
        self.root.mainloop()
