import discord
from discord.ext import commands

class Example(commands.Cog):

    ##### initalization #####
    def __init__(self, client):
        self.client = client

    ##### events #####
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"User '{member}' has joined the server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"User '{member}' has left the server.")
    
    ##### tasks #####

    ##### commands #####
    @commands.command(aliases=['pong', 'latency'])
    async def ping(self, ctx):
        embed = discord.Embed(
            description = f'I currently operate at an latency of {round(self.client.latency * 1000)}ms',
            colour = discord.Colour.blue()
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['cls', 'clean', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1): # dangerous! - clears the chat by a specified amount of messages
        await ctx.channel.purge(limit=amount+1)
        print(f'Cleared up to {amount} messages in #{ctx.channel} ')
    
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.bot.logout()
        print(f"Shutdown")

##### finalize and run #####
def setup(client):
    client.add_cog(Example(client))
