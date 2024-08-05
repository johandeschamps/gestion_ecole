from dataclasses import dataclass

from src.inputable import Inputable


@dataclass
class Note(Inputable):
    student_id = None
    course_id = None
    note = None

    def update_grade(self, new_note):
        self.note = new_note

    def get_note_details(self):
        return {
            "student_id": self.student_id,
            "course_id": self.course_id,
            "note": self.note
        }

    def __str__(self):
        return f"Note(Student ID: {self.student_id}, Course ID: {self.course_id}, Grade: {self.note})"