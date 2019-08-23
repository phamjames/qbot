import discord
from discord.ext.commands import Bot
import asyncio
import random
import secrets
from commands import *
from utility import *


#initialize bot
client = Bot(command_prefix='$',description='This bot invites people to play games.')

# lobbies
lobbies = {}


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.email)
    print(client.user.name)
    print(client.user.id)
    print("------------")

    
@client.event
async def on_message(message):
    #ignore messages sent by the bot (listen for user messages)
    if message.author == client.user:
        return

    #parse user input
    user_input = {}
    if message.content.startswith(client.command_prefix):
        print(message.content)
        user_input = parse_command(message.content)

    #check if user sent a valid command
    if user_input["command"] in commands.keys():
        await commands[user_input["command"]](message, user_input["arguments"],client)



client.run(secrets.token)