from .outputs import WordleError
from .gameStates import State
from .game import WordleGame 
from .renderer import Renderer

class Wordle:
    def __init__(self) -> None:
        self._setup()

    def _setup(self):
        self.state = State.PLAYING
        self.game = WordleGame()
        self.renderer = Renderer()
    
    def start(self):
        print("Welcome to command line wordle!")
        print("correct letters and placings are wrapped with *: [ * a * ]")
        print("correct letters but incorrect placings are wrapped with ~: [ ~ a ~ ]")
        print()
        # loop games and await game states
        while not self.isEnd():
            guess = input("Guess a 5 letter word >>  ")
            res = self.game.process(guess)
            if not isinstance(res, WordleError):
                self.update()

            if self.isEnd():
                self.end()
                return

    def setState(self):
        if self.game.triesRemaining == 0:
            if self.game.isWin:
                self.state = State.WIN
            else:
                self.state = State.COMPLETED
        elif self.game.isWin:
            self.state = State.WIN
    
    def update(self):
        self.setState()
        self.renderer.render(self.game.responses)
        print("Tries remaining: ", self.game.triesRemaining)

    def isEnd(self):
        return self.state in [State.COMPLETED, State.WIN]

    def end(self):
        print("\n")
        if self.state == State.WIN:
            print("Congratulations you have guessed the right word!")
        print(f"The game has ended in {WordleGame.MAX_TRIES - self.game.triesRemaining} tries.")
        print(f"The secret word is {self.game.answer}")
        print("\nWhat would you like to do next?")

        choice = input("Enter p to play again and any other key to quit >>  ")
        if choice == "p":
            self._setup()
            self.start()
        return