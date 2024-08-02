from abc import *
from dataclasses import *

@dataclass
class UserInput(ABC):

    @abstractmethod
    def userInput(self) -> bool:
        """
        Fills out the object's fields based on user intput
        :return: if the input was sucessful
        """

        ...