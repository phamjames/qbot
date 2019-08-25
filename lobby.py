import discord
import asyncio
import os
import time


class Lobby:
    def __init__(self, owner, title, description, client):
        self.owner = owner
        self.title = title
        self.description = description
        self.client = client
        self.game = None
        self.time = None
        self.players = {str(self.owner)}
        self.accepted = len(self.players)
        self.declined = 0
        self._parse_title()

    def _title_checker(self,title):
        return

    def _description_checker(self,descr):
        return

    def _parse_title(self):
        split_title = self.title.split("@")
        self.game = split_title[0]
        self.time = split_title[1]

    def embed(self):
        embed = discord.Embed(title=self.title, description=self.description, color=0xbb22ee)
        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/premium/png-256-thumb/video-game-3-510444.png")
        embed.add_field(name="Players accepted: " + str(self.accepted), value = "\n".join(self.players), inline = False)
        return embed
