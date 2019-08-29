import secrets
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from commands import commands
import utility
from utility import *
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

@loop(seconds=10)
async def check_time():
    if lobbies:
        now = datetime.now()
        for lobby in utility.sorted_lobbies:
            print(lobby.title)
            #check if lobby time is about 10 minutes from now
            ten_min_later = now + timedelta(minutes=10)
            #if 10 min from now is within 15s of or after lobby time, we execute
            print(lobby.time - ten_min_later)
            if timedelta(minutes=-10) <= lobby.time - ten_min_later <= timedelta(seconds=10):
                channel=bot.get_channel(485385917373087760)
                alert = (lobby.title + ' starts soon.') + (" Get on {}".format(" ".join(["<@{}>".format(i.id) for i in lobby.players])))
                await channel.send(alert)
                print('ping people')
        print("------------")

bot.run(secrets.token)
