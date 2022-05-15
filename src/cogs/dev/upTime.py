import discord
from discord.ext import commands
from time import time
from datetime import timedelta
from ...lib.perms import isOwner, PermissionDeniedEmbed


class upTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time()

    @discord.slash_command()
    async def uptime(self, ctx):
        if not isOwner(ctx.author.id):
            await PermissionDeniedEmbed(ctx)
            return

        differenceInTime = time()-self.start_time
        text = str(timedelta(seconds=differenceInTime))
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Uptime', value=text)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(upTime(bot))
