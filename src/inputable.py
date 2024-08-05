from abc import *
from dataclasses import *
from typing import Protocol


class Inputable(Protocol):
    def user_input(self) -> bool:
        """
        Fills out the object's fields based on user intput
        :return: if the input was sucessful
        """

        ...
