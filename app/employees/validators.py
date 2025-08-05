from typing import Optional
from pydantic import BaseModel, field_validator
from sqlalchemy.orm import Session

from .models import Employee
from .schemas import EmployeeSchema, FULL_NAME_PATTERN


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
        if value != FULL_NAME_PATTERN:
            raise ValueError(
                'Имя написано со строчной буквы '
                'или использованы недопустимые символы'
            )
        return value

    @field_validator('surname', mode='after')
    def validate_surname(cls, value: str) -> str:
        """Валидация фамилии."""
        if value != FULL_NAME_PATTERN:
            raise ValueError(
                'Фамилия написана со строчной буквы '
                'или использованы недопустимые символы'
            )
        return value

    @field_validator('patronymic', mode='after')
    def validate_patronymic(cls, value: Optional[str]) -> Optional[str]:
        """Валидация отчества."""
        if value:
            if value != FULL_NAME_PATTERN:
                raise ValueError(
                    'Отчество написано со строчной буквы '
                    'или использованы недопустимые символы'
                )
        return value if value else None


def validate_employee(data: EmployeeSchema) -> bool:
    """Полная функция валидации сотрудника"""
    EmployeeValidator(**data)

    return True
