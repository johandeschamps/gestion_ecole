import typing
from dataclasses import dataclass
from datetime import datetime, date
from typing import List

from src.inputable import Inputable
from src import inputs

if typing.TYPE_CHECKING:
    from src.student import Student


@dataclass
class Course(Inputable):
    """
    A class to represent a course.

    Attributes
    ----------
    name : str
        The name of the course.
    begin_date : date
        The start date of the course.
    end_date : date
        The end date of the course.
    """
    name: str
    begin_date: date
    end_date: date
    students: List['Student']

    def user_input(self) -> bool:
        self.name = input("Nom : ")
        self.begin_date = inputs.date("Date de commencement : ")
        self.end_date = inputs.date("Date de fin : ")

        return True

    def remove_student(self, student: 'Student'):
        assert self in student.courses
        assert student in self.students

        student.courses.remove(self)
        self.students.remove(student)

    def add_student(self, student: 'Student'):
        assert self not in student.courses
        assert student not in self.students

        student.courses.append(self)
        self.students.append(student)

    def input_course_details(self) -> str:
        """
        Prompts the user to input the course details and returns a formatted string.

        Returns
        -------
        str
            A string containing the course name, begin date, and end date.
        """
        self.name = input("Nom de cours : ")
        begin_date_str = input("Date de commencement du cours(YYYY-MM-DD): ")
        end_date_str = input("Date de fin du cours: (YYYY-MM-DD): ")
        self.begin_date = datetime.strptime(begin_date_str, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        return f"Cours: {self.name}, date de commencement: {self.begin_date},  date de fini: {self.end_date}"

    def current_course(self, date: date) -> None:
        """
        Checks if the course is active on the given date.

        Parameters
        ----------
        date : date
            The date to check against the course's begin and end dates.
        """
        if self.begin_date <= date <= self.end_date:
            print("ce cours a commençé")
        else:
            print("ce cours est fini ou il n'a pas encore commençé")
