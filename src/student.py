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

        self.id = int(input("Id étudiant: "))

        return True

    def get_note(self, course: Course) -> Note:
        """Get the student note for a course or create an empty one if none exists"""
        if self not in course.students:
            raise KeyError("Student not part of this course")

        for note in self.notes:
            if note.course == course:
                return note

        new_note = Note(self, course, 0)
        self.notes.append(new_note)
        return new_note

    def get_course(self, name: str) -> Optional[Course]:
        for course in self.courses:
            if course.name.lower().strip() == name.lower().strip():
                return course
        return None

    def __str__(self):
        return f"Étudiant: {self.first_name} {self.last_name}, Âge: {self.age}, Adresse: {self.address}, ID: {self.id}, Cours: {[course.name for course in self.courses]}, Notes: {self.notes}"
