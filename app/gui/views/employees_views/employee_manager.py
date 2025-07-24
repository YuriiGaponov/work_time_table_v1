from app.gui.views.base import BaseModalView


class EmployeeManagerView(BaseModalView):
    """Окно работы со списком сотрудников."""

    def __init__(self, top_view):
        super().__init__(top_view)
