import time
import keyboard
import pydirectinput
import os
import ProfileManager

#takes the user message as a parameter.
wasSomethingPressed = False

def KeyboardInputs(message):
    testMessage = message.lower()
    with open("backend/profiles/" + ProfileManager.profile + ".txt") as f:
        for l_no, lines in enumerate(f):
            if testMessage in lines:
                singleLine = lines
                singleLine = singleLine.split(",")
                inputType = str(singleLine[0]).lower()
                duration = str(singleLine[1]).lower()
                keyword = str(singleLine[2]).lower()
                keybind = str(singleLine[3]).lower()[:-1]
                if(testMessage==keyword):
                    if(inputType) == "press":
                        pressKeyNew(keybind)
                    elif(inputType.lower()) == "hold":
                        holdKey(keybind, duration)    

    '''
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
    '''     

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

    file1 = open("backend/profiles/" + ProfileManager.profile + ".txt", "a")
    if holdOrPress.lower() == 'hold':
        newLine = holdOrPress + "," + duration + "," + chosenKeyword + "," + allocatedKeybind
    else:
        newLine = holdOrPress + "," + "nil" + "," + chosenKeyword + "," + allocatedKeybind 
    file1.write(str(newLine)+'\n')
    file1.close()

def deleteKeybind():
    deleteKeyword = input("Which keyword do you want to delete?: ")
    with open("backend/profiles/" + ProfileManager.profile + ".txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if deleteKeyword not in i:
                f.write(i)
        f.truncate()
    
# def pressKey(key):
#     keyboard.press(key)
#     keyboard.release(key)

def pressKeyNew(key):
    pydirectinput.press(key)
    global wasSomethingPressed 
    wasSomethingPressed = True

def holdKey(key, seconds):
    currentTime = time.time()
    trackTime = currentTime
    futureTime = currentTime + float(seconds)
    print(currentTime)
    while trackTime<=futureTime:
        trackTime = time.time()
        pydirectinput.press(key)
    pydirectinput.keyUp(key)

        
def typeMessage(inputMessage):
    for x in inputMessage:
        keyboard.press(x,3)

def somethingWasPressed():
    return wasSomethingPressed