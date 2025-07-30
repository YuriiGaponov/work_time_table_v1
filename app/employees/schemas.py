import re
from typing import TypedDict, Optional


class EmployeeSchema(TypedDict):
    """Строго типизированный словарь для данных сотрудника"""
    name: str
    patronymic: Optional[str]
    surname: str
    department: str


# Ф.И.О. может состоять из нескольких слов, разделенных дефисом или пробелом,
# после дефиса идет заглавная или строчная буква
FULL_NAME_PATTERN = re.compile(
    r'^[А-ЯЁ][а-яё\s-]*(?:[\s-][А-ЯЁа-яё][а-яё\s-]*)*[а-яё]$'
)
