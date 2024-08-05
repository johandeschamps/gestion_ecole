from dataclasses import dataclass
from datetime import datetime

from inputable import Inputable


@dataclass
class Course(Inputable):
    """
    A class to represent a course.

    Attributes
    ----------
    name : str
        The name of the course.
    begin_date : datetime
        The start date of the course.
    end_date : datetime
        The end date of the course.
    """
    name: str
    begin_date: datetime
    end_date: datetime

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

    def current_course(self, date: datetime) -> None:
        """
        Checks if the course is active on the given date.

        Parameters
        ----------
        date : datetime
            The date to check against the course's begin and end dates.
        """
        if self.begin_date < date < self.end_date:
            print("This course is active")
        else:
            print("The course is already finished or has not started yet")
