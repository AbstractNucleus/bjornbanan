import discord
from discord.ext import commands
from discord.commands import slash_command, SlashCommandGroup
import os


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

            cogs.append(path)

            '''try:
                bot.load_extension(path)

            except Exception as e:
                ans = input(f"{path} could not be loaded. Print error? ('y' or 'n')\n")
                if ans == "y":
                    raise (e)

                ans = input(f"Exclude {path} and continue? ('y' or 'n')\n")
                if ans == "n":
                    exit()'''

        return bot

    cogs = SlashCommandGroup("cogs", "Managing cogs")

    @cogs.command()
    async def list(self, ctx):
        await ctx.respond("Byebye")


def setup(bot):
    bot.add_cog(CogManagement(bot))
