import re
from config import *
from lobby import Lobby
from exceptions import *


async def start(message, arguments, client):
    #split the arguments to get params for a new lobby
    try:
        owner = message.author
        parsed_args = _parse_arguments(arguments)
    except IncorrectTitleFormat:
        await message.channel.send(TITLE_FORMAT_INCORRECT)
    except DescriptionTooLong:
        await message.channel.send(DESCR_TOO_LONG)
    else:
        title, description = parsed_args[0], parsed_args[1]
        new_lobby = Lobby(owner,title,description,client)
        await message.channel.send(embed=new_lobby.embed())



def _parse_arguments(args):
    ''' This function will parse the arguments and split them into
        title and description.
        It will return the two as a tuple -> (title, description) '''
    #split arguments into title and description
    split_args = args.split()
    print(split_args[1:])
    title = _check_title(split_args[0])
    description = _check_description((" ").join(split_args[1:]))
    return (title,description)



def _check_title(title):
    title_pattern = re.compile(r"^\w+@(1[0-2]|[1-9])(:[0-5][0-9])?(am|pm)$")
    match = title_pattern.match(title.lower())

    if match:
        return title
    raise IncorrectTitleFormat



def _check_description(descr):
    print(descr)
    if len(descr) <= MAX_DESCRIPTION_LENGTH:
        return descr
    raise DescriptionTooLong