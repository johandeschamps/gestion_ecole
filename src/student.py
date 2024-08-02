import dataclasses
from dataclasses import *
from typing import List

from src.course import Course
from src.note import Note
from src.person import Person


@dataclass
class Student(Person):
    id: int
    courses: List[Course] = field(default_factory=lambda: [])

    def user_input(self) -> bool:
        super().user_input()

        self.id = int(input("Student id: "))

        return True

    def get_note(self, course: Course) -> Note:
        ...

    def get_course(self, name: str) -> Course:
        ...
