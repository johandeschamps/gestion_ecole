from abc import *
from dataclasses import *

from src.address import Address


@dataclass
class Person(ABC):
    first_name : str
    last_name : str
    age : int
    address : Address