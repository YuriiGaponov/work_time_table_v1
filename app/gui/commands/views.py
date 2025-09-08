"""
Команды открытия окон приложения.
"""

from app.gui.views import BaseView, BaseModalView


def open_modal_view(
        top_view: BaseView,
        ViewModel: BaseModalView
) -> None:
    """Открыть вызываемое окно."""
    view: BaseModalView = ViewModel(top_view)
    view.run()


def open_info_view(
        info: str,
        top_view: BaseView,
        ViewModel: BaseModalView
) -> None:
    """Открыть вызываемое окно с сообщением."""
    view: BaseModalView = ViewModel(top_view)
    view.root_head_lable.config(text=info)
    view.run()
