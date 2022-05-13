import discord
from discord.ext import commands

class exampleCog(commands.Cog): 

    def __init__(self, bot):
        self.bot = bot




def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(exampleCog(bot)) # add the cog to the bot