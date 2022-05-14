import discord
from discord.ext import commands
import os


def initBot(bot):
    bot.load_extension("src.cogs.dev.cogs.managing")
    return bot


def nbot(prefix):

    bot = initBot(
        discord.Bot(
            debug_guilds=[802298523214938153],
            help_command=commands.MinimalHelpCommand(),
            command_prefix=prefix,
            intents=discord.Intents.all(),
        )
    )

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")

    return bot
