from dataclasses import *

from src.inputable import UserInput


@dataclass
class Address(UserInput):
    postal_code: int
    city: str
    street_name: str

    def user_input(self) -> bool:
        self.city = input("City: ")
        self.postal_code = int(input("Postal code: ").strip())
        self.street_name = input("Street name: ")

        return True
