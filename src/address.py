from dataclasses import *

@dataclass
class Address:
    postal_code : int
    city : str
    street_name : str