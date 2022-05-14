import discord
from discord.ext import commands

cogs = [
    'testing.fabian.git'
]


def createBot():
    bot = commands.Bot(
        debug_guilds=[802298523214938153], help_command=commands.MinimalHelpCommand(), intents=discord.Intents.all())

    for cog in cogs:
        bot.load_extension(f'src.cogs.{cog}')

    return bot
