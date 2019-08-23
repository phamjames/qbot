from lobby import Lobby

async def start(message, arguments, client):
    split_args = arguments.split()
    owner = message.author
    title = split_args[0]
    description = (" ").join(split_args[1:])
    new_lobby = Lobby(owner,title,description,client)

    await message.channel.send(embed=new_lobby.embed())