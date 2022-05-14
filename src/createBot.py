import discord
from discord.ext import commands


def initBot(bot):
    dev = ["cogs", "upTime", "git", "presence", "rateLimit"]
    [bot.load_extension(f"src.cogs.dev.{i}") for i in dev]
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
