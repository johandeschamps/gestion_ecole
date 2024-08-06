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

    def input_course_details(self) -> str:
        """
        Prompts the user to input the course details and returns a formatted string.

        Returns
        -------
        str
            A string containing the course name, begin date, and end date.
        """
        self.name = input("Name of course: ")
        begin_date_str = input("Begin date of course (YYYY-MM-DD): ")
        end_date_str = input("End date of course (YYYY-MM-DD): ")
        self.begin_date = datetime.strptime(begin_date_str, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

        return f"Course: {self.name}, Begin date: {self.begin_date}, End date: {self.end_date}"

    def current_course(self, date: date) -> None:
        """
        Checks if the course is active on the given date.

        Parameters
        ----------
        date : date
            The date to check against the course's begin and end dates.
        """
        if self.begin_date < date < self.end_date:
            print("This course is active")
        else:
            print("The course is already finished or has not started yet")
