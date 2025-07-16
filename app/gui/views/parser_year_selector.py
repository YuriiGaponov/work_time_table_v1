from .base import BaseView
from .config import ParserYearSelectorViewConfig


class ParserYearSelector(BaseView):
    """Окно выбора года для парсинга календаря."""

    def __init__(self):
        super().__init__()
        self.root.title(ParserYearSelectorViewConfig.TITLE)
        self.root_lable.config(text=ParserYearSelectorViewConfig.HEAD_LABLE)
