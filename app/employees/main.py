from sqlalchemy.orm import Session
from .models import Employee
from .schemas import EmployeeSchema


def employee_exist(session: Session, data: EmployeeSchema) -> bool:
    """Проверяет, существует ли сотрудник в БД."""
    return session.query(Employee).filter(
        Employee.name == data['name'],
        Employee.patronymic == data['patronymic'],
        Employee.surname == data['surname'],
        Employee.department == data['department']
    ).first() is not None


def save_employee(session: Session, data: EmployeeSchema):
    """Сохраняет данные сотрудника в БД."""
    session.add(
        Employee(
            name=data['name'],
            patronymic=data['patronymic'],
            surname=data['surname'],
            department=data['department']
        )
    )
    session.commit()
