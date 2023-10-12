import KeyboardInputs
from random import randint

def test_inputTriggers():
    randomNumber = randint(1, 100)
    if (randomNumber % 2 == 0):
        KeyboardInputs.pressKeyNew('w')
        assert KeyboardInputs.somethingWasPressed()
    else:
        assert not KeyboardInputs.somethingWasPressed()