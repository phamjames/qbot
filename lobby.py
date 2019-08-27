import discord
import re
from config import *
from exceptions import IncorrectTitleFormat, DescriptionTooLong

lobbies = dict()

class Lobby:
    def __init__(self, owner, title, description):
        self.owner = owner
        self.title = self._check_title(title)
        self.description = self._check_description(description)
        self.game = None
        self.time = None
        self.players = set()
        self.has_emoji = False
        self._parse_title()

    def _parse_title(self):
        split_title = self.title.split("@")
        self.game = split_title[0]
        self.time = split_title[1]

    def _check_title(self,title):
        title_pattern = re.compile(r"^\w+@(1[0-2]|[1-9])(:[0-5][0-9])?(am|pm)$")
        match = title_pattern.match(title.lower())

        if match:
            return title
        raise IncorrectTitleFormat

    def _check_description(self,descr):
        if len(descr) <= MAX_DESCRIPTION_LENGTH:
            return descr
        raise DescriptionTooLong


    def embed(self):
        embed = discord.Embed(title=self.title, description=self.description, color=0xbb22ee)
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/premium/png-256-thumb/video-game-3-510444.png")
        embed.add_field(name="Players accepted: " + str(len(self.players)), value = "None" if not self.players else "\n".join(self.players), inline = False)
        return embed
