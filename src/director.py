from typing import List
from dataclasses import dataclass, field
from person import Person
from student import Student
from teacher import Teacher
from course import Course
from address import Address


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

    def modify_course(self, course: Course, name: str, start_date: str, end_date: str):
        if course in self.courses:
            if name:
                course.name = name
            if start_date:
                course.start_date = start_date
            if end_date:
                course.end_date = end_date
        else:
            raise ValueError("This course is not registered.")

    def extend_course_date(self, course: Course, new_end_date: str):
        if course in self.courses:
            course.end_date = new_end_date
        else:
            raise ValueError("This course is not registered.")

    def add_student(self, student: Student):
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError("This student is already registered.")

    def remove_student(self, student: Student):
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("This student is not in the list.")

    def add_teacher(self, teacher: Teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            raise ValueError("This teacher is already registered.")

    def remove_teacher(self, teacher: Teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
        else:
            raise ValueError("This teacher is not in the list.")

    def modify_student_info(self, student: Student, first_name: str, last_name: str, age: int, address: str):
        if student in self.students:
            if first_name:
                student.first_name = first_name
            if last_name:
                student.last_name = last_name
            if age:
                student.age = age
            if address:
                student.address = address
        else:
            raise ValueError("This student is not registered.")

    def modify_teacher_info(self, teacher: Teacher, first_name: str, last_name: str, age: int, address: Address, entry_date: str):
        if teacher in self.teachers:
            if first_name:
                teacher.first_name = first_name
            if last_name:
                teacher.last_name = last_name
            if age:
                teacher.age = age
            if address:
                teacher.address = address
            if entry_date:
                teacher.entry_date = entry_date
        else:
            raise ValueError("This teacher is not registered.")

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError("This course already exists.")
