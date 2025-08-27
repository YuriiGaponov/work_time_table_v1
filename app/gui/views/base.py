import tkinter as tk
from tkinter import ttk


class BaseConfig():
    """Базовый класс настроек окон приложения."""

    TITLE: str = 'Базовое название окна'
    HEAD_LABLE: str = 'Базовый заголовок'
    STICKY: str = 'NSEW'


class BaseView():
    """Базовый класс окна приложения."""

    def __init__(self, master=None):
        """Инициализация окна."""
        self.root = master or tk.Tk()
        self.root.title(BaseConfig.TITLE)

        # Фрейм для размещения заголовка окна
        self.root_head_frame = ttk.Frame(self.root)
        self.root_head_frame.pack()

        self.root_head_lable = ttk.Label(
            self.root_head_frame, text=BaseConfig.HEAD_LABLE
        )
        self.root_head_lable.grid(row=0, column=0, sticky=BaseConfig.STICKY)

        # Фрейм для размещения контента
        self.root_content_frame = ttk.Frame(self.root)
        self.root_content_frame.pack()

    def run(self):
        """Запуск окна."""
        self.root.mainloop()


class BaseModalView(BaseView):
    """Базовый класс вызываемого окна."""

    def __init__(self, top_view: BaseView):
        super().__init__(master=tk.Toplevel(top_view.root))
        self.top_view = top_view

        self.root.transient(top_view.root)
        self.root.grab_set()


class BaseErrorView(BaseModalView):
    """Базовый класс окна сообщений об ошибках."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)

        self.confirm_button = ttk.Button(
            self.root_content_frame,
            text='ОК',
            command=self.confirm
        )
        self.confirm_button.grid(row=0, column=0, sticky=BaseConfig.STICKY)

    def confirm(self):
        """Подтвердить прочтение сообщения об ошибке и закрыть окно."""
        self.root.destroy()


class BaseListView(BaseModalView):
    """Базовый класс окна со списком."""

    def __init__(self, top_view, items=None):
        """Инициализация окна."""
        super().__init__(top_view)
        self.items = items if items is not None else []

        self.listbox = tk.Listbox(
            self.root_content_frame
        )

        self.listbox.pack()
