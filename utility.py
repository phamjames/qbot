from config import *


async def add_checkin(message,lobbies):
    if message.author.name == bot_name and message.embeds:
        lobby_title = message.embeds[0].title
        if lobby_title in lobbies and not lobbies[lobby_title].has_emoji:
            await message.add_reaction(WHITE_HEAVY_CHECK_MARK)
            curr_lobby = lobbies[lobby_title]
            curr_lobby.has_emoji = True

async def checkin_player(reaction,user,lobbies):
    message = reaction.message
    if message.author.name == bot_name and message.embeds:
        lobby_title = message.embeds[0].title
        if lobby_title in lobbies and not user.name == bot_name:
            curr_lobby = lobbies[lobby_title]
            curr_lobby.players.add(user.name)
            await message.edit(embed=curr_lobby.embed())

async def checkout_player(reaction,user,lobbies):
    message = reaction.message
    if message.author.name == bot_name and message.embeds:
        lobby_title = message.embeds[0].title
        curr_lobby = lobbies[lobby_title]
        curr_lobby.players.remove(user.name)
        await message.edit(embed=curr_lobby.embed())

def add_commands_to_bot(bot, commands):
    for command in commands:
        bot.add_command(command)
