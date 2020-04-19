from config import *
import operator

sorted_lobbies = []

async def add_checkin(message,lobbies):
    if message.author.name == bot_name and message.embeds:
        lobby_title = message.embeds[0].title
        if lobby_title in lobbies and not lobbies[lobby_title].has_emoji:
            await message.add_reaction(WHITE_HEAVY_CHECK_MARK)
            curr_lobby = lobbies[lobby_title]
            curr_lobby.has_emoji = True
            curr_lobby.message = message
            await message.pin()
            #now sort the lobbies into a list after adding a new one
            global sorted_lobbies
            sorted_lobbies = sorted(lobbies.values(), key=operator.attrgetter('time'))

async def checkin_player(reaction,user,lobbies):
    message = reaction.message
    if message.author.name == bot_name and message.embeds:
        emoji  = reaction.emoji
        if emoji != WHITE_HEAVY_CHECK_MARK:
            await reaction.message.remove_reaction(emoji,user)
            return
        lobby_title = message.embeds[0].title
        if lobby_title in lobbies and not user.name == bot_name:
            curr_lobby = lobbies[lobby_title]
            curr_lobby.players.add(user)
            await message.edit(embed=curr_lobby.embed())

async def checkout_player(reaction,user,lobbies):
    message = reaction.message
    if message.author.name == bot_name and message.embeds:
        emoji = reaction.emoji
        if emoji != WHITE_HEAVY_CHECK_MARK:
            return
        lobby_title = message.embeds[0].title
        curr_lobby = lobbies[lobby_title]
        curr_lobby.players.remove(user)
        await message.edit(embed=curr_lobby.embed())

async def check_time(lobbies):
    if lobbies:
        for lobby in utility.sorted_lobbies:
            #check if lobby time is coming up in status is pending
            if lobby.status == PENDING:
                #check if lobby time is about 10 minutes from now
                now = datetime.now()
                ten_min_later = now + timedelta(minutes=10)
                #if 10 min from now is within 15s of or after lobby time, we execute
                if timedelta(minutes=-10) <= lobby.time - ten_min_later <= timedelta(seconds=5):
                    alert=(lobby.title + ' starts soon.') + (" {}".format(" ".join(["<@{}>".format(i.id) for i in lobby.players])))
                    await lobby.message.channel.send(alert)
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
                    await lobby.message.unpin()

def add_commands_to_bot(bot, commands):
    for command in commands:
        bot.add_command(command)
