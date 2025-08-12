from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import Optional, List

from .models import Employee
from .schemas import EmployeeSchema


def search_employees(
    session: Session,
    name: Optional[str] = None,
    patronymic: Optional[str] = None,
    surname: Optional[str] = None,
    department: Optional[str] = None
) -> List[Employee]:
    """
    Поиск сотрудников по одному или нескольким полям.
    """
    query = session.query(Employee)

    filters = []

    if name:
        filters.append(Employee.name.ilike(f'%{name}%'))

    if patronymic:
        filters.append(Employee.patronymic.ilike(f'%{patronymic}%'))

    if surname:
        filters.append(Employee.surname.ilike(f'%{surname}%'))

    if department:
        filters.append(Employee.department == department)

    if filters:
        query = query.filter(and_(*filters))

    return query.all()


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
