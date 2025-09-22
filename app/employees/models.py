from sqlalchemy import Column, String, UniqueConstraint

from app.db import Base


class Employee(Base):
    """Класс для хранения сведений о сотруднике."""

    name: str = Column(String)
    patronymic: str = Column(String, nullable=True)
    surname: str = Column(String)
    department: str = Column(String)

    __table_args__ = (
        UniqueConstraint(
            'name', 'patronymic', 'surname', 'department',
            name='ux_employee'
        ),
    )

    def __init__(self, name: str, surname: str, department: str,
                 patronymic: str = None):
        """Конструктор для создания нового сотрудника."""
        self.name = name
        self.surname = surname
        self.department = department
        self.patronymic = patronymic

    def initials(self) -> str:
        """Возвращает инициалы сотрудника в формате Фамилия И.О."""
        initials = f'{self.surname} {self.name[0]}.'
        if self.patronymic:
            initials += f'{self.patronymic[0]}.'
        return initials
