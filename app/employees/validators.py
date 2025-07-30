from typing import Optional
from pydantic import BaseModel, field_validator, ValidationError

from .schemas import FULL_NAME_PATTERN


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
            if not value.strip():
                raise ValidationError(
                    'Отчество написано со строчной буквы',
                    ' или использованы недопустимые символы'
                )
        return value if value else None
