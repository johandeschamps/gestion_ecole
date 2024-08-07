from dataclasses import *

from src.inputable import Inputable


@dataclass
class Address(Inputable):
    postal_code: int
    city: str
    street_name: str

    def user_input(self) -> bool:
        self.city = input("Ville: ")
        self.postal_code = int(input("Code postal: ").strip())
        self.street_name = input("Nom de la rue: ")

        return True

    def __str__(self):
        return f"Nom de rue: {self.street_name}, Ville: {self.city}, Code postal: {self.postal_code}"
