
from typing import List
from dataclasses import dataclass, field
from person import Person
from student import Student
from teacher import Teacher
from course import Course


@dataclass
class Director(Person):

        students: List[Student] = field(default_factory=list)
        teachers: List[Teacher] = field(default_factory=list)
        courses: List[Course] = field(default_factory=list)

  def get_students(self) -> List[Student]:
            return self.students

 def get_teachers(self) -> List[Teacher]:
            return self.teachers

 def get_courses(self) -> List[Course]:
            return self.courses
