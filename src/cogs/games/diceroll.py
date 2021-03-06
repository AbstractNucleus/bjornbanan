import discord
from discord.ext import commands
from random import randint


class diceRoll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def diceroll(self, ctx, sides: int = 6):
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(
            name=f'You rolled a {sides} sided dice', value=f'and got {randint(1,sides)}')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(diceRoll(bot))
