import socket
import threading
import time
import KeyboardInputs


##Global variables
global user
global message

##Server and port information
SERVER = "irc.twitch.tv"
PORT = 6667

##OAuth token and bot account information
##tokens can be found here... https://twitchapps.com/tmi/
PASS = "oauth:acg413d5tln1omi9omb72lbkgje0e1"
NICK = "CCG_Bot".lower()
CHANNEL = "nekonatic".lower()

##Initialize socket and connect to Twitch IRC server
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(f"PASS {PASS}\nNICK {NICK}\nJOIN #{CHANNEL}\n".encode())

#Allows twitch while loop to be paused.
pauseEvent = threading.Event()
#Allows twitch while loop to be paused.
exitEvent = threading.Event()

def twitch():
    """
    Handles the Twitch chat interaction.
    """

    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            if "PING :tmi.twitch.tv" in line:
                msgg = "PONG :tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                continue
            else:
                user = getUser(line)
                message = getMessage(line)
                if user == "" or user == " ":
                    continue
                print(user.title() + " : " + message)
                KeyboardInputs.KeyboardInputs(message)

        if exitEvent.is_set():
            False
            break

        if pauseEvent.is_set():
            False
        elif pauseEvent.is_set() == False:
            True



def joinchat():
    """
    Joins the Twitch chat.
    """
    Loading = True
    while Loading:
        readbuffer_join = irc.recv(1024).decode()
        for line in readbuffer_join.split("\n")[:-1]:
            Loading = loadingComplete(line)


def loadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True    

def sendMessage(irc, message):
    messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
    irc.send((messageTemp + "\n").encode())


def getUser(line):
    colons = line.count(":")
    separate = line.split(":", colons)
    user = separate[1].split("!", 1)[0]
    return user


def getMessage(line):
    try:
        colons = line.count(":")
        message = (line.split(":", colons))[colons]
    except:
        message = ""
    return message


##Start the Twitch bot
##t1 = threading.Thread(target=twitch)
##t1.start()