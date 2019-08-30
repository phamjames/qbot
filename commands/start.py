from discord.ext import commands
from config import *
from lobby import Lobby, lobbies
from exceptions import *


@commands.command(name='start')
async def start(ctx, *args):
    #split the arguments to get params for a new lobby
    try:
        owner = ctx.message.author

        parsed_args = _parse_arguments(args)
        title, description = parsed_args[0], parsed_args[1]
        new_lobby = Lobby(owner, title, description)
        _add_to_lobbies(new_lobby)

    except IncorrectTitleFormat:
        await ctx.send(TITLE_FORMAT_INCORRECT)
    except DescriptionTooLong:
        await ctx.send(DESCR_TOO_LONG)
    except LobbyAlreadyExists:
        await ctx.send(LOBBY_ALREADY_EXISTS)
    else:
        await ctx.send(embed=new_lobby.embed())


def _add_to_lobbies(lobby):
    if not lobbies:
        lobbies[lobby.title] = lobby
    else:
        if lobby.title in lobbies:
            raise LobbyAlreadyExists
        else:
            lobbies[lobby.title] = lobby

def _parse_arguments(args):
    ''' This function will parse the arguments and split them into
        title and description.
        It will return the two as a tuple -> (title, description) '''

    title = args[0]
    description = " ".join(list(args[1:]))

    return (title,description)
