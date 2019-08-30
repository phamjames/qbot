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
async def check_time():
    if lobbies:
        for lobby in utility.sorted_lobbies:
            #check if lobby time is coming up in status is pending
            if lobby.status == PENDING:
                #check if lobby time is about 10 minutes from now
                now = datetime.now()
                ten_min_later = now + timedelta(minutes=10)
                #if 10 min from now is within 15s of or after lobby time, we execute
                if timedelta(minutes=-10) <= lobby.time - ten_min_later <= timedelta(seconds=5):
                    channel=bot.get_channel(485385917373087760)
                    alert=(lobby.title + ' starts soon.') + (" {}".format(" ".join(["<@{}>".format(i.id) for i in lobby.players])))
                    await channel.send(alert)
                    lobby.status=ACTIVE
                    print(lobby.message.content)
                    await lobby.message.edit(embed=lobby.embed())

            elif lobby.status == ACTIVE:
                now = datetime.now()
                if now >= lobby.time:
                    lobby.status=LIVE
                    await lobby.message.edit(embed=lobby.embed())

            else:
                now = datetime.now()
                two_hours_later = now + timedelta(hours=2)
                if lobby.time >= two_hours_later:
                    utility.sorted_lobbies.remove(lobby)
                    lobbies.pop(lobby.title)
                    lobby.status=EXPIRED
                    await lobby.message.edit(embed=lobby.embed())


bot.run(secrets.token)