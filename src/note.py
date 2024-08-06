from dataclasses import dataclass

from src.inputable import Inputable


@dataclass
class Note(Inputable):
    student: 'Student'
    course: 'Course'
    note: float

    def update_grade(self, new_note):
        self.note = new_note

    def get_note_details(self):
        return {
            "student_id": self.student.id,
            "course_name": self.course.name,
            "note": self.note
        }

    def __str__(self):
        return f"Note(Student ID: {self.student.id}, Course Name: {self.course.name}, Grade: {self.note})"
