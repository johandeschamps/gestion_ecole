from abc import *
from dataclasses import *

from src.address import Address
from src.user_input import UserInput


@dataclass
class Person(UserInput):
    first_name: str
    last_name: str
    age: int
    address: Address

    def userInput(self) -> bool:
        self.first_name = input("First name: ")
        self.last_name = input("Last name: ")
        self.age = int(input("Age: "))
        self.address.userInput()

        return True
