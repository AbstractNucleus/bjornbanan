import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, Option
import os
from asyncio import sleep


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

    return cogs


class CogLoaderView(discord.ui.View):

    @discord.ui.select(
        placeholder="Load",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=i) for i in getAllCogs()]
    )
    async def select_callback(self, select, interaction):
        try:
            try:
                interaction.client.load_extension(select.values[0])
                await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Loaded", color=0x00FF42))

            except discord.errors.ExtensionAlreadyLoaded as e:
                await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Already loaded", color=0xFD3333))

        except Exception as e:
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} is broken and cannot load", color=0xFD3333))


class CogUnloaderView(discord.ui.View):

    @discord.ui.select(
        placeholder="Unload",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=i) for i in getAllCogs()]
    )
    async def select_callback(self, select, interaction):
        try:
            interaction.client.unload_extension(select.values[0])
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Unloaded", color=0x00FF42))

        except discord.errors.ExtensionNotLoaded:
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Not loaded", color=0xFD3333))


class CogReloaderView(discord.ui.View):

    @discord.ui.select(
        placeholder="Reload",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=i) for i in getAllCogs()]
    )
    async def select_callback(self, select, interaction):
        try:
            try:
                interaction.client.unload_extension(select.values[0])
                interaction.client.load_extension(select.values[0])

            except:
                interaction.client.load_extension(select.values[0])

            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Reloaded", color=0x00FF42))

        except Exception as e:
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} is broken and cannot load", color=0xFD3333))


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
    async def load(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Unloader", color=0x00FF42), view=CogLoaderView())

    @cogs.command()
    async def unload(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Unloader", color=0x00FF42), view=CogUnloaderView())

    @cogs.command()
    async def reload(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Reloader", color=0x00FF42), view=CogReloaderView())

    @cogs.command()
    async def reloadall(self, ctx):
        for cog in getAllCogs():
            if cog == "src.cogs.dev.cogs.managing":
                continue
            try:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog)

            except:
                self.bot.load_extension(cog)

        await ctx.edit(embed=discord.Embed(title=f"All cogs have been reloaded", color=0x00FF42))

    # not done

    @cogs.command()
    async def loadall(self, ctx):
        await ctx.respond("Hello, this is a slash subcommand from a cog!")


def setup(bot):
    bot.add_cog(CogManagement(bot))
