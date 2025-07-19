from ..base import BaseErrorView
from .config import IncorrectYearViewConfig


class IncorrectYearView(BaseErrorView):
    """Информационное окно с сообщение о неверном вводе года."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(IncorrectYearViewConfig.TITLE)
