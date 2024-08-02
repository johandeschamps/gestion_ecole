from abc import *
from dataclasses import *

from src.address import Address
from src.inputable import Inputable


@dataclass
class Person(Inputable):
    first_name: str
    last_name: str
    age: int
    address: Address

    def user_input(self) -> bool:
        self.first_name = input("First name: ")
        self.last_name = input("Last name: ")
        self.age = int(input("Age: "))
        print("# Address :")
        self.address.user_input()
        print("-")
        return True
