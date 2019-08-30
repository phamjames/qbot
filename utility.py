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

def add_commands_to_bot(bot, commands):
    for command in commands:
        bot.add_command(command)
