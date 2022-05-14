import discord
from discord.ext import commands
import os


def loadAllCogs(bot):
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
        try:
            bot.load_extension(path)
        except Exception as e:
            ans = input(f"{path} could not be loaded. Print error?\n")
            if ans:
                for x, y in enumerate(e):
                    pass
    return bot


def nbot(prefix):

    bot = loadAllCogs(
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
