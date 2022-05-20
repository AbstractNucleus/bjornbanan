from dotenv import load_dotenv
from os import getenv
from discord.ext import commands
import discord

load_dotenv()


def isOwner():
    async def predicate(ctx):
        if str(ctx.author.id) not in getenv("OWNERS"):
            await ctx.respond(embed=discord.Embed(title=f"You do not have permission to use that command!!!", color=0xFD3333))
        else:
            return str(ctx.author.id) in getenv("OWNERS")
    return commands.check(predicate)
