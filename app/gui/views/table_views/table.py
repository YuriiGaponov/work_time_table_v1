from app.gui.views.base import BaseListView, BaseModalView
from .config import TableViewConfig, TableSelectorViewConfig


class TableSelectorView(BaseModalView):
    """Окно выбора табеля."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(TableSelectorViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableSelectorViewConfig.HEAD_LABLE
        )


class TableView(BaseListView):
    """Окно отображения табеля."""

    def __init__(self, top_view):
        super().__init__(top_view)
        self.root.title(TableViewConfig.TITLE)
        self.root_head_lable.config(
            text=TableViewConfig.HEAD_LABLE
        )
