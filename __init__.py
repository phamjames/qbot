import discord
from discord.ext.commands import Bot
import asyncio
import random
import secrets
from utility import *


#initialize bot
client = Bot(command_prefix='$',description='This bot invites people to play games.')

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.email)
    print(client.user.name)
    print(client.user.id)
    print("------------")

    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.startswith(client.command_prefix):




client.run(secrets.token)