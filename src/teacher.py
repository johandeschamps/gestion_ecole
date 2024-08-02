import datetime
from dataclasses import *
from typing import List

from src.course import Course
from src.note import Note
from src.person import Person
from src.student import Student


@dataclass
class Teacher(Person):
    entry_date: datetime.date
    course: Course

    def get_note(self, student: Student) -> Note:
        """

        :param student:
        :return: The student's note, created if it not exists
        """
        ...

    def get_students(self) -> List[Student]:
        ...

    def user_input(self) -> bool:
        super().user_input()
        self.entry_date = datetime.date.fromisoformat(input("Entry date (YYYY-MM-DD) : "))
        # TODO : Course
