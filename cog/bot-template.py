import discord
from discord.ext import commands

class BotTemplate(commands.Cog):

    ##### initalization #####
    def __init__(self, client):
        self.client = client

##### finalize and run #####
def setup(client):
    client.add_cog(BotTemplate(client))
