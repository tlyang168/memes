from collections import Counter
import random
from .outputs import (
    Response,
    WordleError,
    ValueStates
)
from .wordBanks import (
    WORD_BANK,
    ALLOWED_WORD_BANK,
)

class WordleGame:
    MAX_TRIES = 6

    def __init__(self):
        self.answer = WORD_BANK.get(random.choice(list(WORD_BANK.keys())))
        self.triesRemaining = WordleGame.MAX_TRIES
        self.guesses = []
        self.responses = []
        self.isWin = False

    def validate(self, guess):
        error = None
        if len(guess) != 5:
            error = WordleError(f"Guess has to be 5 letters, got {len(guess)}")
            return False, error
        if guess not in ALLOWED_WORD_BANK:
            error = WordleError(f"{guess} is not a valid word")
            return False, error
        return True, error
        

    def getDiffResponse(self, guess):
        # 0. check if guess is right
        if guess == self.answer:
            self.isWin = True

        # 1. check if letter is in guess
        guessLetters = Counter(guess)
        trueLetters = Counter(self.answer)
        coloredLetters = set(guessLetters.keys()).intersection(trueLetters.keys())

        # 2. check if letter is in correct position
        seen = dict([(k, 0) for k in coloredLetters])
        encoding = [ValueStates.REGULAR] * 5
        for (i, letter) in enumerate(guess):
            if letter in coloredLetters:
                if self.answer[i] == letter:
                    encoding[i] = ValueStates.GREEN
                    seen[letter] += 1
                else:
                    # check seen quantity of this letter against answer
                    if seen[letter] + 1 <= trueLetters[letter]:
                        encoding[i] = ValueStates.YELLOW
                        seen[letter] += 1
        response = Response(guess, encoding)
        return response


    def process(self, guess):
        isValid, error = self.validate(guess)
        if not isValid:
            # don't decrement remaining tries and error
            return error
        response = self.getDiffResponse(guess)
        self.responses.append(response)
        self.triesRemaining -= 1
        return response