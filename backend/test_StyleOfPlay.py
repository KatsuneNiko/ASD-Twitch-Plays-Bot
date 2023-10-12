import TwitchConnect
import pytest
from random import randint

def test_getCurrentStyle():
    defaultStyleOfPlay = TwitchConnect.getStyleOfPlay()
    assert defaultStyleOfPlay == "anarchy" and not defaultStyleOfPlay == "democratic"

def test_styleOfPlayChanged():
    randomNumber = randint(1, 100)
    if (randomNumber % 2 == 0):
        anarchyOrDemocratic = "anarchy"
    else:
        anarchyOrDemocratic = "democratic"

    oldStyleOfplay = TwitchConnect.styleOfPlay
    
    if(anarchyOrDemocratic == 'anarchy'):
        if(anarchyOrDemocratic != TwitchConnect.styleOfPlay):
            TwitchConnect.setStyleOfPlay(anarchyOrDemocratic, 0)
            assert oldStyleOfplay != anarchyOrDemocratic
        else:
            assert oldStyleOfplay == anarchyOrDemocratic
    else:
        if(anarchyOrDemocratic != TwitchConnect.styleOfPlay):
            TwitchConnect.setStyleOfPlay(anarchyOrDemocratic, 0)
            assert oldStyleOfplay != anarchyOrDemocratic
        else:
            assert oldStyleOfplay == anarchyOrDemocratic

            