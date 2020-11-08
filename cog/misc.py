import json
import datetime

import discord
from discord.ext import commands

config = json.load(open("config.json"))["yggdrasil-misc"] # Needs to be the same as in `config.json`!

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def echo(self, ctx, *, input='Hello World!'):
        embed = discord.Embed(
            title = input,
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx, *, input='Hello World!'):
        embed = discord.Embed(
            description = f'{input}',
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def datecounter(self, ctx, *, input=''):
        today = datetime.date.today()
        if input == '':
            someday = datetime.date(2019, 11, 18)
        else:
            input = input.split('-')
            someday = datetime.date(int(input[0]), int(input[1]), int(input[2]))
        diff = today - someday

        embed = discord.Embed(
            title = 'Datecounter',
            description = f'Days: {diff.days}',
            colour = discord.Colour.blue()
        )
        embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    @commands.command()
    async def fibonacci(self, ctx, *, input='1'):
        if not input.isdigit():
            return
        al = []
        a, b = 0, 1
        while len(al) < int(input)+1:
            al.append(a)
            a, b = b, a+b
        embed = discord.Embed(
            title = 'Fibonacci',
            description = f'{input}. Fibonacci number: {al[int(input)]}',
            colour = discord.Colour.blue()
        )
        embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

    # write backwards
    @commands.command(aliases=['backwards', 'invert'])
    async def reverse(self, ctx, *, input='Lagerregal'):
        output = ''
        for x in range(0, len(input)):
            output = input[x] + output
        embed = discord.Embed(
            title = 'Write backwards',
            colour = discord.Colour.blue()
        )
        embed.set_author(name=f'{ctx.author}', icon_url=f'{ctx.author.avatar_url}')
        embed.add_field(name='Input', value=f'{input}', inline=False)
        embed.add_field(name='Reversed', value=f'{output}', inline=False)
        await ctx.send(embed=embed)

##### finalize and run #####
def setup(client):
    client.add_cog(Misc(client))
