from typing import Optional
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session

from .models import Employee
from .schemas import EmployeeSchema, FULL_NAME_PATTERN
from .validation_messages import EmployeeValidatorMesseges


def employee_exist(session: Session, data: EmployeeSchema) -> bool:
    """Проверяет, существует ли сотрудник в БД."""
    return session.query(Employee).filter(
        Employee.name == data['name'],
        Employee.patronymic == data['patronymic'],
        Employee.surname == data['surname'],
        Employee.department == data['department']
    ).first() is not None


class EmployeeValidator(BaseModel):
    """Модель для валидации данных сотрудника."""

    name: str
    patronymic: Optional[str] = None
    surname: str
    department: str

    @field_validator('name', mode='after')
    def validate_name(cls, value: str) -> str:
        """Валидация имени."""
        if value and not FULL_NAME_PATTERN.match(value):
            raise ValueError(EmployeeValidatorMesseges.NAME_PATTERN_MISMATCH)
        return value

    @field_validator('surname', mode='after')
    def validate_surname(cls, value: str) -> str:
        """Валидация фамилии."""
        if value and not FULL_NAME_PATTERN.match(value):
            raise ValueError(
                EmployeeValidatorMesseges.SURNAME_PATTERN_MISMATCH
            )
        return value

    @field_validator('patronymic', mode='after')
    def validate_patronymic(cls, value: Optional[str]) -> Optional[str]:
        """Валидация отчества."""
        if value and not FULL_NAME_PATTERN.match(value):
            raise ValueError(
                EmployeeValidatorMesseges.PATRONYMIC_PATTERN_MISMATCH
            )
        return value if value else None


def validate_employee(data: EmployeeSchema) -> bool:
    """Полная функция валидации сотрудника"""
    EmployeeValidator(**data)

    return True
