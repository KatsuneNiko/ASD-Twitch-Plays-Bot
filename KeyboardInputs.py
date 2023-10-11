import socket
import threading
import time
import keyboard
import pydirectinput
import os
import datetime

#takes the user message as a parameter.
def KeyboardInputs(message):
    testMessage = message.lower()
    totalMessages = []
    with open('KeywordsToKeyboard.txt') as f:
        for l_no, validKeybinds in enumerate(f):
            readSingleLine = validKeybinds
            readSingleLine = readSingleLine.split(",")
            readKeyword = str(readSingleLine[2]).lower()
            if testMessage in readKeyword:
                singleLine = validKeybinds
                singleLine = singleLine.split(",")
                inputType = str(singleLine[0]).lower()
                duration = str(singleLine[1]).lower()
                keyword = str(singleLine[2]).lower()
                keybind = str(singleLine[3]).lower()[:-1]
                playWithAnarchyMode(inputType, keybind, duration)  

def playWithDemocraticMode(message):
    democraticStarted = False
    endTime = None
    myList = []
    if democraticStarted == False:
                    myList.clear()
                    democraticStarted = True
                    endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
                    myList.append(message)
    elif democraticStarted == True:
        if datetime.datetime.now() >= endTime:
            mostCommon = most_frequent(myList)
            KeyboardInputs(mostCommon)
            myList.clear()
            myList.append(message)
            endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)
        else:
            myList.append(message)

def playWithAnarchyMode(holdOrPress, key, potentialTime):
    time = potentialTime ##make sure to validate in frontend
    if(holdOrPress) == "press":
        pressKeyNew(key)
    elif(holdOrPress.lower()) == "hold":
        holdKey(key, time) 

def most_frequent(List):
    return max(set(List), key = List.count)

def addKeybind():
    holdOrPress = ""
    ##Validation: user must only be able to select hold or press.
    while holdOrPress.lower() != "hold" and holdOrPress.lower() != "press":
        os.system('cls')
        holdOrPress = input("Hold or Press?: ")
        if holdOrPress.lower() != "hold" and holdOrPress.lower() != "press":
            os.system('cls')
            print("Invalid answer, \"" + holdOrPress + "\" is not a valid answer, please try again. ")
            input("Press any key to continue... ")
        else:
            break

    if holdOrPress.lower() == 'hold':
        ##Validation: user must only be able to select ints or valid floats
        duration = input("Duration in seconds? e.g. 1 or 1.5: ")
    ##Validation: can not be an existing duplicate
    chosenKeyword = input("Input exact keyword: ")
    ##Validation: valid keyboard bind
    allocatedKeybind = input("What key is this binded to?: ")

    file1 = open("KeywordsToKeyboard.txt", "a")
    if holdOrPress.lower() == 'hold':
        newLine = holdOrPress + "," + duration + "," + chosenKeyword + "," + allocatedKeybind
    else:
        newLine = holdOrPress + "," + "nil" + "," + chosenKeyword + "," + allocatedKeybind 
    file1.write(str(newLine)+'\n')
    file1.close()

def deleteKeybind():
    deleteKeyword = input("Which keyword do you want to delete?: ")
    with open("KeywordsToKeyboard.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if deleteKeyword not in i:
                f.write(i)
        f.truncate()
    
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