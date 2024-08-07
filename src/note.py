import typing
from dataclasses import dataclass

from src.inputable import Inputable

if typing.TYPE_CHECKING:
    from src.student import Student
    from src.course import Course


@dataclass
class Note(Inputable):
    student: 'Student'
    course: 'Course'
    note: float

    def user_input(self) -> bool:
        self.note = float(input("Note (ex 13.0) : "))

        return True

    def update_grade(self, new_note):
        self.note = new_note

    def get_note_details(self):
        return {
            "student_id": self.student.id,
            "course_name": self.course.name,
            "note": self.note
        }

    def __str__(self):
        return f"Note(Id étudiant: {self.student.id}, Nom cours: {self.course.name}, Note: {self.note})"
