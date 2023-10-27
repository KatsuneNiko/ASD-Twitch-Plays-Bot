import subprocess
import os
import platform
import os
import discord
import TwitchConnect
import KeyboardInputs
import datetime

accessToken = 'MTE2MjM0NTkyNDc5ODk4ODI5OA.GcWWz4.WcMk2lNI29zoAp3OU1fcRCNYAM93fwfOm2I1KE'
nickname = 'CCGchatbot'
channelJoin = "Mew's Palace"

# bot.py

intents = discord.Intents.all() # Create an instance of Intents
client = discord.Client(intents=intents) #pass the intents

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=channelJoin)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

democraticStarted = False
endTime = None
myList = []

@client.event
async def on_message(message):
    global democraticStarted
    global endTime
    message_content = message.content
    message_author = message.author
    print(f'New message -> {message_author} said: {message_content}')
    #Call the keyboard input functions
    if TwitchConnect.styleOfPlay == 'anarchy':
        KeyboardInputs.KeyboardInputs(message_content)
    elif TwitchConnect.styleOfPlay == 'democratic':
        while TwitchConnect.styleOfPlay == 'democratic':
            if democraticStarted == False:
                myList.clear()
                democraticStarted = True
                endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
                myList.append(message_content)
            elif democraticStarted == True:
                if datetime.datetime.now() >= endTime:
                    ##print("Total messages: ", *myList)
                    mostCommon = most_frequent(myList)
                    KeyboardInputs.KeyboardInputs(mostCommon)
                    myList.clear()
                    myList.append(message_content)
                    endTime = datetime.datetime.now() + datetime.timedelta(seconds=3)
                else:
                    myList.append(message_content)

def returnMessage():
    global messageTest
    discordMessage = messageTest
    return discordMessage

def runDiscordBot():
    client.run(accessToken)

def most_frequent(List):
    return max(set(List), key = List.count)
