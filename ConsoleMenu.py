import os
import threading
import TwitchConnect
import KeyboardInputs

if __name__ == '__main__':
    userInput = ''
    currentProfile = ''
    t1 = threading.Thread(target=TwitchConnect.twitch)
    ##t2 = TwitchConnect.twitch()

    while userInput != 'exit':
        print("Twitch Plays Bot v2")
        if currentProfile != '':
            print("Currently loaded profile: " + currentProfile)
        else:
            print("No profile currently loaded. Select or create a profile to get started")
        print("1 - Select/create profile")
        print("2 - Delete current profile")
        print("3 - Start chatbot")
        print("4 - Stop chatbot")
        print("5 - View keybinds")
        print("6 - Add keybind")
        print("7 - Delete keybind")
        print("exit - Exit program")
        userInput = input("Input one of the above: ")
        os.system('cls')
        match userInput:
            case '1':
                tempProfile = input("Input the profile you'd like to use (case sensitive): ")
                if os.path.exists("profiles/" + tempProfile + ".txt"):
                    print("Profile " + tempProfile + " has been selected")
                    currentProfile = tempProfile
                else:
                    createNew = input("Unable to find profile. Create a new profile with name " + tempProfile + "? (yes/no) ")
                    if createNew.lower() == 'yes':
                        open("profiles/" + tempProfile + ".txt", 'x')
                        print("Profile " + tempProfile + " has been created")
                        currentProfile = tempProfile
                    else:
                        print("Profile was not created")
                input("Press any key to continue... ")

            case '2':
                if os.path.exists("profiles/" + currentProfile + ".txt"):
                    deleteConfirmation = input("Are you sure you would like to delete profile " + currentProfile + "? (yes/no) ")
                    if deleteConfirmation.lower() == 'yes':
                        os.remove("profiles/" + currentProfile + ".txt")
                        print("Profile " + currentProfile + " has been deleted")
                        currentProfile = ''
                    else:
                        print("Profile deletion has been cancelled")
                else:
                    print("Unable to find current profile")
                input("Press any key to continue... ")

            case '3':
                if os.path.exists("profiles/" + currentProfile + ".txt"):
                    KeyboardInputs.profile = currentProfile
                    if t1.is_alive() and TwitchConnect.pauseEvent.is_set() == False:
                        print("Chatbot is already active")
                    elif t1.is_alive() and TwitchConnect.pauseEvent.is_set() == True:
                        TwitchConnect.pauseEvent.clear()
                        print("Chatbot has now been restarted")
                    else:
                        t1.daemon = True
                        t1.start()
                        os.system('cls')
                        print("Chatbot is now active")
                else:
                    print("Unable to find current profile")
                input("Press any key to continue... ")
            
            case '4':
                if t1.is_alive():
                    TwitchConnect.pauseEvent.set()
                    print("Chatbot has been stopped")
                else:
                    print("Chatbot was not active")
                input("Press any key to continue... ")

            case '5':
                if os.path.exists("profiles/" + currentProfile + ".txt"):
                    if os.path.getsize("profiles/" + currentProfile + ".txt") > 0:
                        f = open("profiles/" + currentProfile + ".txt", "r")
                        print(f.read())
                    else:
                        print("No keybinds exist in current profile")
                else:
                    print("Unable to find current profile")
                input("Press any key to continue... ")

            case '6':
                if os.path.exists("profiles/" + currentProfile + ".txt"):
                    KeyboardInputs.profile = currentProfile
                    KeyboardInputs.addKeybind()
                    print("Success!")
                else:
                    print("Unable to find current profile")
                input("Press any key to continue... ")

            case '7':
                if os.path.exists("profiles/" + currentProfile + ".txt"):
                    KeyboardInputs.profile = currentProfile
                    KeyboardInputs.deleteKeybind()
                    print("Success!")
                else:
                    print("Unable to find current profile")
                input("Press any key to continue... ")

            case 'exit':
                TwitchConnect.exitEvent.set()
                pass

        os.system('cls')