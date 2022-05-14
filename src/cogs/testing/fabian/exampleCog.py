import discord
from discord.ext import commands, bridge


class exampleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command()
    async def hello(self, ctx, a: int, b: str):
        print(ctx)
        await ctx.respond(f"d4g, this is a discord comm{sum}and from a{b} cog!")

    @commands.command()
    async def bbb(self, ctx):
        print(ctx)
        await ctx.message.respond(f'monkey')


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(exampleCog(bot))  # add the cog to the bot
