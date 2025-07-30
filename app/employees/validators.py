from typing import Optional
from pydantic import BaseModel, field_validator, ValidationError
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

    @field_validator('name', mode='before')
    def validate_name(cls, value: str) -> str:
        if value != FULL_NAME_PATTERN:
            raise ValidationError(
                'Имя написано со строчной буквы',
                ' или использованы недопустимые символы'
            )
        return value

    @field_validator('surname', mode='before')
    def validate_surname(cls, value: str) -> str:
        if value != FULL_NAME_PATTERN:
            raise ValidationError(
                'Фамилия написана со строчной буквы',
                ' или использованы недопустимые символы'
            )
        return value

    @field_validator('patronymic', mode='before')
    def validate_patronymic(cls, value: Optional[str]) -> Optional[str]:
        if value:
            if value != FULL_NAME_PATTERN:
                raise ValidationError(
                    'Отчество написано со строчной буквы',
                    ' или использованы недопустимые символы'
                )
        return value if value else None


def validate_employee(session: Session, data: EmployeeSchema) -> bool:
    """Полная функция валидации сотрудника"""
    try:
        # Валидация через Pydantic
        validated_data = EmployeeValidator(**data)
        
        return True
    
    except ValidationError as ve:
        print(f"Ошибка валидации данных: {ve}")
        return False
