from sqlalchemy.orm import Session
from .models import Employee
from .schemas import EmployeeSchema


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
