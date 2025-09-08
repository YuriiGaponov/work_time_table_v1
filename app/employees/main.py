from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import List

from .models import Employee
from .schemas import EmployeeSchema


def search_employees(
    session: Session,
    data: EmployeeSchema
) -> List[Employee]:
    """
    Поиск сотрудников по одному или нескольким полям.
    """
    query = session.query(Employee)

    filters = []

    if data.get('name'):
        filters.append(Employee.name.ilike(f'%{data["name"]}%'))

    if data.get('patronymic'):
        filters.append(Employee.patronymic.ilike(f'%{data["patronymic"]}%'))

    if data.get('surname'):
        filters.append(Employee.surname.ilike(f'%{data["surname"]}%'))

    if data.get('department'):
        filters.append(Employee.department == data["department"])

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
