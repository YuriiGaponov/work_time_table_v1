from app.gui.views import BaseView
from app.gui.views.employees_views import EmployeeManagerView


def open_employee_manager(top_view: BaseView) -> None:
    """Открыть окно управления данными сотрудников."""
    employee_manager = EmployeeManagerView(top_view)
    employee_manager.run()
