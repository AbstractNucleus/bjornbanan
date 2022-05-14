import discord
from discord.ext import commands
from git import Repo
import os


class Git(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def gitpull(self, ctx):
        if not str(ctx.author.id) == "243022798543519745" and not str(ctx.author.id) == "212483159659380739":
            await ctx.respond(embed=discord.Embed(title="You dont have access to this command", color=0xFD3333))
            return

        try:
            repo = Repo(os.getcwd())
            repo.git.pull()
            await ctx.respond(embed=discord.Embed(title="Successfully pulled", color=0x00FF42))
        except:
            await ctx.respond(embed=discord.Embed(title="Failed to pull", color=0xFD3333))


def setup(bot):
    bot.add_cog(Git(bot))
