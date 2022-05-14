import discord
from discord.ext import commands


class presence(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def changepresence(self, ctx):
        await ctx.respond(f'yes')


def setup(bot):
    bot.add_cog(presence(bot))
