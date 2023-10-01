import os
import threading
import TwitchConnect


userInput = ''
t1 = threading.Thread(target=TwitchConnect.twitch)
##t2 = TwitchConnect.twitch()

while userInput != 'exit':
    print("Main menu")
    print("Press the following to trigger function")
    print("1 - Start chatbot")
    print("2 - Stop chatbot")
    print("3 - Open txt. file")
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

        case 'exit':
            TwitchConnect.exitEvent.set()
            pass

    os.system('cls')