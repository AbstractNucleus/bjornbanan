import discord
from discord.ext import commands, bridge


class exampleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command()
    async def hello(self, ctx, a: discord.Option(int)):
        sum = a
        await ctx.respond(f"newest, this is a discord comm{sum}and from a cog!")


def setup(bot):  # this is called by Pycord to setup the cog
    bot.add_cog(exampleCog(bot))  # add the cog to the bot
