from dataclasses import dataclass


from person import Person
from address import Address
from student import Student
from teacher import Teacher
from course import Course


@dataclass
class Director(Person):
    
