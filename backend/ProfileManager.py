import os
import KeyboardInputs as KeyboardInputs

profile = 'WASD'

def profileExists(name):
    return os.path.exists("backend/profiles/" + name + ".txt")

def selectProfileGUI():
    global profile
    tempProfile = input("Input the profile you'd like to use (case sensitive): ")
    if profileExists(tempProfile):
        print("Profile " + tempProfile + " has been selected")
        profile = tempProfile
    else:
        createNew = input("Unable to find profile. Create a new profile with name " + tempProfile + "? (yes/no) ")
        if createNew.lower() == 'yes':
            createProfile(tempProfile)
        else:
            print("Profile was not created")

def selectProfile(name):
    global profile
    profile = name

def createProfile(name):
    global profile
    open("backend/profiles/" + name + ".txt", 'x')
    print("Profile " + name + " has been created")
    profile = name

def deleteProfileGUI():
    global profile
    if profileExists(profile):
        deleteConfirmation = input("Are you sure you would like to delete profile " + profile + "? (yes/no) ")
        if deleteConfirmation.lower() == 'yes':
            deleteProfile(profile)
        else:
            print("Profile deletion has been cancelled")
    else:
        print("Unable to find current profile")

def deleteProfile(name):
    global profile
    os.remove("backend/profiles/" + name + ".txt")
    print("Profile " + name + " has been deleted")
    profile = ''

def viewProfile():
    global profile
    if profileExists(profile):
        if os.path.getsize("backend/profiles/" + profile + ".txt") > 0:
            f = open("backend/profiles/" + profile + ".txt", "r")
            print(f.read())
        else:
            print("No keybinds exist in current profile")
    else:
        print("Unable to find current profile")

def listProfiles():
    return list(map(lambda x: x.split('.')[0], os.listdir("backend/profiles/")))

def addKeybind():
    global profile
    if profileExists(profile):
        KeyboardInputs.addKeybind()
        print("Success!")
    else:
        print("Unable to find current profile")

def deleteKeybind():
    global profile
    if profileExists(profile):
        KeyboardInputs.deleteKeybind()
        print("Success!")
    else:
        print("Unable to find current profile")