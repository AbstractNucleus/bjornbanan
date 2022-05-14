import discord
from discord.ext import commands


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def enable(self, ctx, hej):
        await ctx.respond(hej)


def setup(bot):
    bot.add_cog(CogManagement(bot))
