import socket
import threading
import time
import keyboard
import TwitchConnect
import pydirectinput



#takes the user message as a parameter.
def KeyboardInputs(message):
    testMessage = message.lower()

    #hardcode keywords to keyboard inputs
    if testMessage == 'hello':
        typeMessage(testMessage)
    elif testMessage == 'up':
        pressKeyNew('w')
    elif testMessage == 'down':
        pressKeyNew('s')
    elif testMessage == 'left':
        pressKeyNew('a')
    elif testMessage == 'right':
        pressKeyNew('d')
    elif testMessage == 'a':
        pressKeyNew('x')
    elif testMessage == 'b':
        pressKeyNew('z')
    elif testMessage == 'start':
        pressKeyNew('o')
    elif testMessage == 'select':
        pressKeyNew('p')
    elif testMessage == 'time':
        print(time.time())

def pressKey(key):
    keyboard.press(key)
    keyboard.release(key)

def pressKeyNew(key):
    pydirectinput.press(key)

def holdKey(key, seconds):
    currentTime = time.time()
    trackTime = currentTime
    futureTime = currentTime + seconds
    print(currentTime)
    while trackTime<=futureTime:
        trackTime = time.time()
        keyboard.press(key)
        keyboard.release(key)

def typeMessage(inputMessage):
    for x in inputMessage:
        keyboard.press(x)