from src.game import WordleGame
from src.outputs import (
    ValueStates,
    Response
)
from src.renderer import Renderer

WINNING_ENCODING = [ValueStates.GREEN] * 5

def isCorrect(expected, observed):
    a = all([e == o for (e, o) in zip(expected, observed)])

    print("passed" if a else "failed")
    return a

def test():
    totalCorrect = 0
    totalTests = 0

    game = WordleGame()
    game.answer = "steak"
    res = game.getDiffResponse("track")
    expected = [1, 0, 1, 0, 2]
    print(f"Test simple: Expected: {expected} Got: {res} ")
    totalCorrect += isCorrect(expected, res.encoding)
    totalTests += 1

    # when 2 letters are present there can be a green and yellow for each letter instance
    game = WordleGame()
    game.answer = "greed"
    res = game.getDiffResponse("stele")
    expected = [0, 0, 2, 0, 1]
    print(f"Test simple: Expected: {expected} Got: {res} ")
    totalCorrect += isCorrect(expected, res.encoding)
    totalTests += 1

    # when only a single letter is present
    # we want to invalidate other guess of same letter, if guessed correctly
    game = WordleGame()
    game.answer = "dream"
    res = game.getDiffResponse("stele")
    expected = [0, 0, 2, 0, 0]
    print(f"Test simple: Expected: {expected} Got: {res} ")
    totalCorrect += isCorrect(expected, res.encoding)
    totalTests += 1

    # we want to make sure that win state is obvious
    game = WordleGame()
    game.answer = "steak"
    res = game.process("steak")

    print(f"Test win: Expected: isWin to be True :  Got: {game.isWin} ")
    totalCorrect += game.isWin == True
    totalTests += 1

    print(f"Passed {totalCorrect} || Failed {totalTests - totalCorrect}")

if __name__ == "__main__":
    test()