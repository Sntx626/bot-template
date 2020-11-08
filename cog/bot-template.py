import json

import discord
from discord.ext import commands

config = json.load(open("config.json"))["bot-template"] # Needs to be the same as in `config.json`!

class BotTemplate(commands.Cog):

    ##### initalization #####
    def __init__(self, client):
        self.client = client

##### finalize and run #####
def setup(client):
    client.add_cog(BotTemplate(client))
