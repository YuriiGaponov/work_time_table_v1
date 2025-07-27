from typing import TypedDict, Optional


class EmployeeSchema(TypedDict):
    """Строго типизированный словарь для данных сотрудника"""
    name: str
    patronymic: Optional[str]
    surname: str
    department: str
