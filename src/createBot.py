import discord
from discord.ext import commands


def initBot(bot):
    bot.load_extension("src.cogs.dev.cogs.managing")
    # bot.load_extension("src.cogs.testing.fabian.presence")
    return bot


def createBot():

    bot = initBot(
        discord.Bot(
            debug_guilds=[802298523214938153],
            help_command=commands.MinimalHelpCommand(),
            intents=discord.Intents.all(),
        )
    )

    @bot.event
    async def on_ready():
        print(
            f"{bot.user} is ready and online with {[i.name for i in bot.walk_application_commands()]}")

    return bot
