import os
import threading
import TwitchConnect as TwitchConnect
import ProfileManager as ProfileManager
import Discordsetup

if __name__ == '__main__':
    userInput = ''
    TwitchConnect.channelname = input("Input the Twitch channel you'd like to connect to: ")
    os.system('cls')
    t1 = threading.Thread(target=TwitchConnect.twitch)
    t2 = threading.Thread(target=Discordsetup.runDiscordBot)
    t2.start()

    while userInput != 'exit':
        print("Twitch Plays Chatbot v2 - " + TwitchConnect.channelname)
        if ProfileManager.profile != '':
            print("Currently loaded profile: " + ProfileManager.profile)
        else:
            print("No profile currently loaded. Select or create a profile to get started")
        if t1.is_alive() and TwitchConnect.pauseEvent.is_set() == False:
            print("Chatbot is active")
        else:
            print("Chatbot is not active")
        print("1 - Select/create profile")
        print("2 - Delete current profile")
        print("3 - Start chatbot")
        print("4 - Stop chatbot")
        print("5 - View keybinds")
        print("6 - Add keybind")
        print("7 - Delete keybind")
        print("8 - Change style of play")
        print("exit - Exit program")
        userInput = input("Input one of the above: ")
        os.system('cls')
        match userInput:
            case '1':
                ProfileManager.selectProfile()
                input("Press any key to continue... ")

            case '2':
                ProfileManager.deleteProfile()
                input("Press any key to continue... ")

            case '3':
                if ProfileManager.profileExists(ProfileManager.profile):
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
                ProfileManager.viewProfile()
                input("Press any key to continue... ")

            case '6':
                ProfileManager.addKeybind()
                input("Press any key to continue... ")

            case '7':
                ProfileManager.deleteKeybind()
                input("Press any key to continue... ")
            case '8':
            ##KeyboardInputs.deleteKeybind()
                userSOPInput = ''
                while userSOPInput != 'success':
                    print("Change the Style of Play")
                    print("Press the following to trigger function")
                    print("1 - Anarchy Mode")
                    print("2 - Democratic Mode")
                    print("cancel - cancel")
                    userSOPInput = input("Input one of the following: ")
                    os.system('cls')
                    match userSOPInput:
                        case '1':
                            TwitchConnect.setStyleOfPlay('anarchy', 0)
                            print("Success! Style of Play is now set to Anarchy")
                            print(TwitchConnect.styleOfPlay)
                            input("Press any key to continue...")
                            userSOPInput = 'success'
                        case '2':
                            print("You have selected Democratic Mode, select the voting duration (in seconds) inbetween every command")
                            userSecondsInput = input("Please select a number between 1-30: ")
                            if userSecondsInput.isnumeric():
                                TwitchConnect.setStyleOfPlay('democratic', userSecondsInput)
                                print("Success! Style of Play is now set to Democratic")
                                print(TwitchConnect.styleOfPlay)
                                userSOPInput = 'success'
                                input("Press any key to continue...")
                            else:
                                print("Error, returning to main menu") 
                                input("Press any key to continue...")
                                userSOPInput = 'success'
                        case 'cancel':
                            userSOPInput = 'success'

            case 'exit':
                TwitchConnect.exitEvent.set()
                pass

        os.system('cls')