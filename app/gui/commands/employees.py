from app.db import session
from app.employees import EmployeeSchema, save_employee
from app.gui.views import BaseView


def open_employee_manager(top_view: BaseView) -> None:
    """Открыть окно управления данными сотрудников."""
    from app.gui.views.employees_views import EmployeeManagerView
    view = EmployeeManagerView(top_view)
    view.run()


def open_create_employee(top_view: BaseView) -> None:
    """Открыть окно добавления нового сотрудника."""
    from app.gui.views.employees_views import CreateEmployeeBaseView
    view = CreateEmployeeBaseView(top_view)
    view.run()


def create_employee(data: EmployeeSchema) -> None:
    """Создать сотрудника и добавить в БД."""
    save_employee(session, data)
