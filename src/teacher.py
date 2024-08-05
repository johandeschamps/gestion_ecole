import datetime
import typing
from dataclasses import *
from typing import List

from src.course import Course
from src.note import Note
from src.person import Person
from src.student import Student


@dataclass
class Teacher(Person):
    entry_date: datetime.date
    courses: List[Course] = field(default_factory=list)

    teachers: typing.ClassVar[List[typing.Self]] = []

    # TODO : Move to course
    def get_note(self, student: Student) -> Note:
        """

        :param student:
        :return: The student's note, created if it not exists
        """
        ...

    def get_course(self, name: str) -> Course:
        ...

    def user_input(self) -> bool:
        super().user_input()
        self.entry_date = datetime.date.fromisoformat(input("Entry date (YYYY-MM-DD) : "))
        return True
