import datetime
import typing
from dataclasses import *
from typing import List

from src import inputs
from src.course import Course
from src.note import Note
from src.person import Person
from src.student import Student


@dataclass
class Teacher(Person):
    entry_date: datetime.date
    courses: List[Course] = field(default_factory=list)

    def get_course(self, name: str) -> typing.Optional[Course]:
        for course in self.courses:
            if course.name.lower().strip() == name.lower().strip():
                return course
        return None

    def user_input(self) -> bool:
        super().user_input()
        self.entry_date = inputs.date("Date d'entrée : ")
        return True

    def __str__(self):
        return super().__str__() + f",Date d'entrée {self.entry_date}"
