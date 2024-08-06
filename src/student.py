import dataclasses
from dataclasses import *
from typing import List, Optional

from src.course import Course
from src.note import Note
from src.person import Person


@dataclass
class Student(Person):
    id: int
    courses: List[Course] = field(default_factory=lambda: [])

    notes: List[Note] = field(default_factory=lambda: [])

    def user_input(self) -> bool:
        super().user_input()

        self.id = int(input("Student id: "))

        return True

    def get_note(self, course: Course) -> Note:
        for ia in self.notes:
            if ia.course == course:
                return ia

        x = Note(self, course, -0)
        self.notes.append(x)
        return x

    def get_course(self, name: str) -> Optional[Course]:
        for i in self.courses:
            if i.name.lower().strip() == name.lower().strip():
                return i

        return None
