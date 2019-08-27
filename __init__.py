import secrets
from discord.ext.commands import Bot
from commands import commands
from utility import *
from lobby import lobbies

# initialize bot
bot = Bot(command_prefix='$',description='This bot invites people to play games.')
add_commands_to_bot(bot,commands)



@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.email)
    print(bot.user.name)
    print(bot.user.id)
    print("------------")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    await add_checkin(message,lobbies)


bot.run(secrets.token)
