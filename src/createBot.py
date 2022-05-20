import discord
from discord.ext import commands


def initBot(bot):
    dev = ["cogs", "git", "presence", "rateLimit", "errorHandling", "info"]
    [bot.load_extension(f"src.cogs.dev.{i}") for i in dev]
    return bot


def createBot():

    bot = initBot(
        discord.Bot(
            help_command=commands.MinimalHelpCommand(),
            intents=discord.Intents.all(),
        )
    )

    @bot.event
    async def on_ready():
        print(
            f"{bot.user} is ready and online with commands: {[i.name for i in bot.walk_application_commands()]}")

    return bot
