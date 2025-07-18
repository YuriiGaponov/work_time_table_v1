import tkinter as tk


class BaseConfig():
    """Базовый класс настроек окон приложения."""

    TITLE: str = 'Базовое название окна'
    HEAD_LABLE: str = 'Базовый заголовок'
    STICKY: str = 'NSEW'


class BaseView():
    """Базовый класс окна приложения."""

    def __init__(self):
        """Инициализация окна."""
        self.root = tk.Tk()
        self.root.title(BaseConfig.TITLE)

        # Фрейм для размещения заголовка окна
        self.root_head_frame = tk.Frame(self.root)
        self.root_head_frame.pack()

        self.root_head_lable = tk.Label(
            self.root_head_frame, text=BaseConfig.HEAD_LABLE
        )
        self.root_head_lable.grid(row=0, column=0, sticky=BaseConfig.STICKY)

        # Фрейм для размещения контента
        self.root_content_frame = tk.Frame(self.root)
        self.root_content_frame.pack()

    def run(self):
        """Запуск окна."""
        self.root.mainloop()


class BaseErrorView(BaseView):
    """Базовый класс окна сообщений об ошибках."""

    def __init__(self):
        """Инициализация окна."""
        super().__init__()

        self.confirm_button = tk.Button(
            self.root_content_frame,
            text='ОК',
            command=self.confirm
        )
        self.confirm_button.grid(row=0, column=0, sticky=BaseConfig.STICKY)

    def confirm(self):
        """Подтвердить прочтение сообщения об ошибке и закрыть окно."""
        self.root.destroy()
