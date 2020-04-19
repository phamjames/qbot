import secrets
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from commands import commands
import utility
from utility import *
from config import *
from lobby import lobbies
from datetime import datetime, timedelta

# initialize bot
bot = Bot(command_prefix='$',description='This bot invites people to play games.')
add_commands_to_bot(bot,commands)


@bot.event
async def on_ready():
    check_time.start()
    print("Logged in as")
    print(bot.user.email)
    print(bot.user.name)
    print(bot.user.id)
    print("------------")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    await add_checkin(message,lobbies)

@bot.event
async def on_reaction_add(reaction, user):
    # will add user to player list
    await checkin_player(reaction,user,lobbies)

@bot.event
async def on_reaction_remove(reaction, user):
    # will remove user to player list
    await checkout_player(reaction,user,lobbies)

@loop(seconds=1)
async def loop_functions():
    await check_time(lobbies)


bot.run(secrets.token)
