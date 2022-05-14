import discord
from discord.ext import commands
from time import time
from datetime import timedelta
start_time = time()


class upTime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def uptime(self, ctx):
        differenceInTime = time()-start_time
        text = str(timedelta(seconds=differenceInTime))
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Uptime', value=text)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(upTime(bot))
