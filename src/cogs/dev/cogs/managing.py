import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
import os


def getAllCogs():
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

    return cogs


class MyView(discord.ui.View):

    @discord.ui.select(
        placeholder="Load a cog",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=i) for i in getAllCogs()]
    )
    async def select_callback(self, select, interaction):
        try:
            interaction.client.load_extension(select.values[0])
            await interaction.response.send_message(embed=discord.Embed(title=f"{select.values[0]} has been loaded", color=0x00FF42))

        except discord.errors.ExtensionAlreadyLoaded as e:
            await interaction.response.send_message(embed=discord.Embed(title=f"{select.values[0]} is already loaded", color=0xFD3333))


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    cogs = SlashCommandGroup("cogs", "Managing cogs")

    @cogs.command()
    async def list(self, ctx):
        string = ""
        for i in getAllCogs():
            string += i+"\n"
        await ctx.respond(string)

    @cogs.command()
    async def load(self, ctx, cog: str):
        print(cog)
        if cog is None:
            await ctx.respond("Yo", view=MyView())
        else:
            print(cog)
            try:
                self.bot.load_extension(cog)
                await ctx.respond(f"{cog} has been loaded")
            except Exception as e:
                raise(e)

    @cogs.command()
    async def unload(self, ctx):

        await ctx.respond("Yo")

    @cogs.command()
    async def loadall(self, ctx):
        await ctx.respond("Hello, this is a slash subcommand from a cog!")


def setup(bot):
    bot.add_cog(CogManagement(bot))
