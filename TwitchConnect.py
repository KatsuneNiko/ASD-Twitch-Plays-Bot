#Required to connect to Twitch
import socket
import threading
import time

#Tell which server and port to connect to, in this case Twitch's server with default port 6667
SERVER = "irc.twitch.tv"
PORT = 6667

#The Twitch OAuth token from the bot account we will be using. Enter manually for now but should be able to be set up
#through the frontend login
PASS = ""

#The nickname of the bot account we're sending messages from. I believe this needs to be lowercase?
NICK = ""
NICK = NICK.lower()

#Channel we're connecting to and reading from
CHANNEL = "KatsuneNiko"
CHANNEL = CHANNEL.lower()

#Connect to Twitch's IRC server and send an encoded message to log into the bot's account and connect to the channel we want
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" + 
          "NICK " + NICK + "\n" + 
          "JOIN #" + CHANNEL + "\n").encode())