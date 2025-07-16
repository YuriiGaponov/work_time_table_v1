import tkinter as tk


class BaseConfig():
    """Базовый класс настроек окон приложения."""

    TITLE: str = 'Базовое название окна'
    HEAD_LABLE: str = 'Базовый заголовок'


class BaseView():
    """Базовый класс окна приложения."""

    def __init__(self):
        """Инициализация окна."""
        self.root = tk.Tk()
        self.root.title(BaseConfig.TITLE)

        # Фрейм для размещения заголовка окна
        self.root_head_frame = tk.Frame(self.root)
        self.root_head_frame.pack()

        self.root_lable = tk.Label(
            self.root_head_frame, text=BaseConfig.HEAD_LABLE
        )
        self.root_lable.pack()

        # Фрейм для размещения контента
        self.root_content_frame = tk.Frame(self.root)
        self.root_content_frame.pack()

    def run(self):
        """Запуск окна."""
        self.root.mainloop()
