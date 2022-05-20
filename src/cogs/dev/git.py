import discord
from discord.ext import commands
from git import Repo
import os
from ...lib.perms import isOwner


class Git(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.command(description="Remote git pull")
    @isOwner()
    async def gitpull(self, ctx):
        try:
            repo = Repo(os.getcwd())
            repo.git.pull()
            await ctx.respond(embed=discord.Embed(title="Successfully pulled", color=0x00FF42))
        except:
            await ctx.respond(embed=discord.Embed(title="Failed to pull", color=0xFD3333))


def setup(bot):
    bot.add_cog(Git(bot))
