from config import *


async def add_checkin(message,lobbies):
    if message.author.name == bot_name and message.embeds:
        lobby_title = message.embeds[0].title
        if lobby_title in lobbies and not lobbies[lobby_title].has_emoji:
            await message.add_reaction(WHITE_HEAVY_CHECK_MARK)
            lobbies[lobby_title].has_emoji = True


def add_commands_to_bot(bot, commands):
    for command in commands:
        bot.add_command(command)