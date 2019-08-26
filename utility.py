from config import *

def parse_command(string):
    '''
    This function will split the command and its arguments and put them into a dictionary
    :param string:
    :return:
    '''
    # remove prefix and split string
    split_string = string[len(prefix):].split()

    return {"command": split_string[0], "arguments": " ".join(split_string[1:])}

def add_commands_to_bot(bot, commands):
    print(commands)
    for command in commands:
        bot.add_command(command)