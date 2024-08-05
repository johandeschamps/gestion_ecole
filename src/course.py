from dataclasses import dataclass
from datetime import datetime

from src.user_input import UserInput


@dataclass
class Course(UserInput):
    """
    A class to represent a course.

    Attributes
    ----------
    name : str
        The name of the course.
    begin_date : int
        The start date of the course.
    end_date : int
        The end date of the course.
    """
    name : str
    begin_date : datetime
    end_date : datetime

    def course(self) -> str:
    """
    Prompts the user to input the course details and returns a formatted string.

    Returns
    -------
    str
            A string containing the course name, begin date, and end date.
    """
        self.name = input("Name of course: ")
        self.begin_date = input("Begin date of course: ")
        self.end_date = input("End date of course: ")
        print (f"Course: {name}, Begin Date: {begin_date}, End Date: {end_date}")


