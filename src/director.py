import datetime
from typing import List, Dict
from dataclasses import dataclass, field
from src.person import Person
from src.student import Student
from src.teacher import Teacher
from src.course import Course
from src.address import Address


@dataclass
class Director(Person):
    """
    A Director manages students, teachers, and courses within an institution.

    Attributes:
        students (List[Student]): List of students managed by the director.
        teachers (List[Teacher]): List of teachers managed by the director.
        courses (List[Course]): List of courses managed by the director.
    """
    students: List[Student] = field(default_factory=list)
    teachers: List[Teacher] = field(default_factory=list)
    courses: List[Course] = field(default_factory=list)

    def get_students(self) -> List[Student]:
        """
        Returns the list of students managed by the director.

        Returns:
            List[Student]: A list of students.
        """
        return self.students

    def get_teachers(self) -> List[Teacher]:
        """
        Returns the list of teachers managed by the director.

        Returns:
            List[Teacher]: A list of teachers.
        """
        return self.teachers

    def get_courses(self) -> List[Course]:
        """
        Returns the list of courses managed by the director.

        Returns:
            List[Course]: A list of courses.
        """
        return self.courses

    def assign_course(self, teacher: Teacher, course: Course):
        """
        Assigns a course to a teacher if both the teacher and course are registered.

        Args:
            teacher (Teacher): The teacher to assign the course to.
            course (Course): The course to assign.

        Raises:
            ValueError: If the teacher is not registered or if the course is not registered,
                        or if the course is already assigned to the teacher.
        """
        if teacher not in self.teachers:
            raise ValueError("L'enseignant n'est pas enregistré..")
        if course not in self.courses:
            raise ValueError("le cours n'est pas enregistré.")
        if course not in teacher.courses:
            teacher.courses.append(course)
        else:
            raise ValueError("le cours a déjà été assigné à l'enseignant")
        if course not in self.courses:
            self.courses.append(course)

    def modify_course(self, course: Course, name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Modifies the details of a registered course.

        Args:
            course (Course): The course to modify.
            name (str): The new name for the course.
            start_date (str): The new start date for the course.
            end_date (str): The new end date for the course.

        Raises:
            ValueError: If the course is not registered.
        """
        if course in self.courses:
            if name:
                course.name = name
            if start_date:
                course.begin_date = start_date
            if end_date:
                course.end_date = end_date
        else:
            raise ValueError("ce cours n'est pas enregistré.")

    def extend_course_date(self, course: Course, new_end_date: datetime.date):
        """
        Extends the end date of a registered course.

        Args:
            course (Course): The course to extend the end date for.
            new_end_date (str): The new end date for the course.

        Raises:
            ValueError: If the course is not registered.
        """
        if course in self.courses:
            course.end_date = new_end_date
        else:
            raise ValueError("ce cours n'est pas enregistré.")

    def add_student(self, student: Student):
        """
        Adds a student to the list of students managed by the director.

        Args:
            student (Student): The student to add.

        Raises:
            ValueError: If the student is already registered.
        """
        if student not in self.students:
            self.students.append(student)
        else:
            raise ValueError("lélève a déjà été  enregistré")

    def remove_student(self, student):
        """
              Removes a student from the list of students managed by the director.

              Args:
                  student (Student): The student to remove.

              Raises:
                  ValueError: If the student is not in the list.
              """
        if student in self.students:
            self.students.remove(student)
        else:
            raise ValueError("l'élève n'est pas dans la liste")

    def add_teacher(self, teacher: Teacher):
        """
        Adds a teacher to the list of teachers managed by the director.

        Args:
            teacher (Teacher): The teacher to add.

        Raises:
            ValueError: If the teacher is already registered.
        """
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            raise ValueError("L'enseignant e déjà été enregistré.")

    def remove_teacher(self, teacher: Teacher):
        """
        Removes a teacher from the list of teachers managed by the director.

        Args:
            teacher (Teacher): The teacher to remove.

        Raises:
            ValueError: If the teacher is not in the list.
        """
        if teacher in self.teachers:
            self.teachers.remove(teacher)
        else:
            raise ValueError("L'enseignant n'est pas dans la list.")

    def modify_student_info(self, student: Student, first_name: str, last_name: str, age: int, address: Address):
        """
        Modifies the information of a registered student.

        Args:
            student (Student): The student to modify.
            first_name (str): The new first name of the student.
            last_name (str): The new last name of the student.
            age (int): The new age of the student.
            address (str): The new address of the student.

        Raises:
            ValueError: If the student is not registered.
        """
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
            raise ValueError("L'élève n'est pas enregistré.")

    def modify_teacher_info(self, teacher: Teacher, first_name: str, last_name: str, age: int, address: Address,
                            entry_date: datetime.date):
        """
        Modifies the information of a registered teacher.

        Args:
            teacher (Teacher): The teacher to modify.
            first_name (str): The new first name of the teacher.
            last_name (str): The new last name of the teacher.
            age (int): The new age of the teacher.
            address (Address): The new address of the teacher.
            entry_date (str): The new entry date of the teacher.

        Raises:
            ValueError: If the teacher is not registered.
        """
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
            raise ValueError("L'enseignant n'est pas enregistré.")

    def add_course(self, course: Course):
        """
        Adds a course to the list of courses managed by the director.

        Args:
            course (Course): The course to add.

        Raises:
            ValueError: If the course already exists.
        """
        if course not in self.courses:
            self.courses.append(course)
        else:
            raise ValueError("ce cours a été déjà enregistré")

    def course_with_teacher(self) -> Dict[str, Dict[str, List[str]]]:
        """
        Provides a summary of courses with assigned teachers and students.

        Returns:
            Dict[str, Dict[str, List[str]]]: A dictionary where the keys are course names and
                                             the values are dictionaries containing teacher's name and list of students.
        """
        result = {}
        for course in self.courses:
            course_info = {
                "teacher": None,
                "students": [student.first_name + " " + student.last_name for student in course.students]
            }
            for teacher in self.teachers:
                if course in teacher.courses:
                    course_info["teacher"] = teacher.first_name + " " + teacher.last_name
                    break
            result[course.name] = course_info
        return result

