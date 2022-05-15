import discord
from discord.ext import commands


class RateLimit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def is_ws_ratelimited(self):
        print("Being websocket ratelimited")


def setup(bot):
    bot.add_cog(RateLimit(bot))
