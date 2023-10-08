import os
import threading
import TwitchConnect
import KeyboardInputs


userInput = ''
t1 = threading.Thread(target=TwitchConnect.twitch)
##t2 = TwitchConnect.twitch()

while userInput != 'exit':
    print("Main menu")
    print("Press the following to trigger function")
    print("1 - Start chatbot")
    print("2 - Stop chatbot")
    print("3 - View Keybinds")
    print("4 - Add keybind")
    print("5 - Delete keybind")
    print("6 - Change style of play")
    print("exit - exit")
    userInput = input("Input one of the following: ")
    os.system('cls')
    match userInput:
        case '1':
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
            input("Press any key to continue...")
        
        case '2':
            if t1.is_alive():
                TwitchConnect.pauseEvent.set()
                print("Chatbot has been stopped")
            else:
                print("Chatbot was not active")
            input("Press any key to continue...")

        case '3':
            f = open("KeywordsToKeyboard.txt", "r")
            print(f.read())
            input("Press any key to continue...")

        case '4':
            KeyboardInputs.addKeybind()
            print("Success!")
            input("Press any key to continue...")
        case '5':
            KeyboardInputs.deleteKeybind()
            print("Success!")
            input("Press any key to continue...")
        case '6':
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