from app.gui.commands import create_employee
from .config import CreateEmployeeBaseViewConfig
from .crud_base_employee import CRUDEmployeeBaseView


class CreateEmployeeBaseView(CRUDEmployeeBaseView):
    """Окно создания нового сотрудника."""

    def __init__(self, top_view):
        """Инициализация окна."""
        super().__init__(top_view)
        self.root.title(CreateEmployeeBaseViewConfig.TITLE)
        self.root_head_lable.config(
            text=CreateEmployeeBaseViewConfig.HEAD_LABLE
        )
        self.confirm_button.config(
            text=CreateEmployeeBaseViewConfig.COMFIRM_BUTTON_TEXT
        )

    def confirn(self):
        create_employee(self, super().confirm())
