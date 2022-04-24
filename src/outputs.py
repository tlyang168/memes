# error 
from enum import Enum, IntEnum

# Value
class ValueStates(IntEnum):
    REGULAR = 0
    YELLOW = 1
    GREEN = 2

class WordleError:
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"WordleError[{self.message}]"

# response from wordle
class Response:
    def __init__(self, guess: str, encoding: ValueStates):
        self.guess = guess
        self.encoding = encoding
    def __str__(self):
        return f"Response[guess[{self.guess}] encoding[{self.encoding}]]"

# rendering formats
class Formats(Enum):
    REGULAR = "[   %s   ] "
    YELLOW = "[ ~ %s ~ ] "
    GREEN = "[ * %s * ] "
