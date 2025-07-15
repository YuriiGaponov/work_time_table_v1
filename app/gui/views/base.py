import tkinter as tk


class BaseView():
    """Базовый класс окн приложения."""

    def __init__(self):
        """Инициализация окна."""
        self.root = tk.Tk()
        self.root.title('Базовое название окна')

        # Фрейм для размещения заголовка окна
        self.root_head_frame = tk.Frame()
        self.root_head_frame.pack()

        self.root_lable = tk.Label(
            self.root_head_frame, text='Базовый заголовок'
        )
        self.root_lable.pack()

        # Фрейм для размещения контента
        self.root_content_frame = tk.Frame()
        self.root_content_frame.pack()

    def run(self):
        """Запуск окна."""
        self.root.mainloop()
