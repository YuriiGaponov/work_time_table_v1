"""
Команды открытия окон приложения.
"""

from typing import Any
from app.gui.views import (
    BaseView,
    BaseListView,
    BaseModalView
)


def open_modal_view(
        top_view: BaseView,
        ViewModel: BaseModalView
) -> None:
    """Открыть вызываемое окно."""
    view: BaseModalView = ViewModel(top_view)
    view.run()


def open_info_view(
        top_view: BaseView,
        ViewModel: BaseModalView,
        info: str = None
) -> None:
    """Открыть вызываемое окно с сообщением."""
    view: BaseModalView = ViewModel(top_view)
    view.root_head_lable.config(text=info)
    view.run()


def open_search_view(
        top_view: BaseView,
        ViewModel: BaseListView,
        search_criteria: Any
) -> None:
    """Открыть окно поиска."""
    view = ViewModel(top_view, search_criteria)
    view.run()
