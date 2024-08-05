
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
             return  self.students


def get_teachers(self) -> List[Teacher]:
            return self.teachers


def get_courses(self) -> List[Course]:
            return self.courses


def get_courses(self) -> List[Course]:
    return self.courses


def assign_course(self, teacher: Teacher, course: Course):
    # Check if the teacher is already in the list of teachers
    if teacher not in self.teachers:
        raise ValueError("The teacher is not registered.")

    # Check if the course is already in the list of courses
    if course not in self.courses:
        raise ValueError("The course is not registered.")

    # Assign the course to the teacher
    if course not in teacher.courses:
        teacher.courses.append(course)
    else:
        raise ValueError("The course is already assigned to this teacher.")

    # Optional: Add the course to the director's list of courses if it's not already present
    if course not in self.courses:
        self.courses.append(course)


def modify_course(self, course: Course, name: str , start_date: str , end_date: str ):
    if course in self.courses:
        if name:
            course.name = name
        if start_date:
            course.start_date = start_date
        if end_date:
            course.end_date = end_date
    else:
        raise ValueError("this course is not already registered")
