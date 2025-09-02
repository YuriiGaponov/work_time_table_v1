from app.gui.views.base import BaseModalView
from .config import TableViewConfig


class TableView(BaseModalView):
    """Окно отображения табеля."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(TableViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableViewConfig.HEAD_LABLE
        )
