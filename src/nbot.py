import discord
from discord.ext import commands
import os


def load_all_cogs(bot):
    paths, cogs = [], []

    for root, subdirs, files in os.walk("src/cogs"):
        if "__pycache__" in subdirs:
            subdirs.remove("__pycache__")

        paths += [os.path.join(root, file) for file in files]

    for i, j in enumerate(paths):
        paths[i] = j.split("/")
        paths[i] = j.split("\\")
        paths[i].remove("src/cogs")
        paths[i][-1] = paths[i][-1][:-3]
        path = "src.cogs"
        for n, m in enumerate(paths[i]):
            path += f".{m}"
        bot.load_extension(path)
    return bot


def nbot(prefix):

    bot = load_all_cogs(
        discord.Bot(
            debug_guilds=[802298523214938153],
            help_command=commands.MinimalHelpCommand(),
            command_prefix=prefix,
            intents=discord.Intents.all()
        )
    )

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")

    return bot
