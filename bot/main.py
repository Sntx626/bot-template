import json
import os

from discord.ext import commands

prefix = json.load(open('config.json'))["default"]["bot_prefix"]
token = json.load(open('config.json'))["default"]["bot_token"]

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print('Ready!')

for f in os.listdir('./cogs'):
    if f.endswith('.py'):
        client.load_extension(f'cogs.{f[:-3]}')

client.run(token)
