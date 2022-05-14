import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup, SlashCommand
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

    return cogs


class CogLoaderView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=20)

    async def on_timeout(self):
        await self.message.delete()

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

            except discord.errors.ExtensionAlreadyLoaded:
                await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Already loaded", color=0xFD3333))

        except Exception as e:
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} is broken and cannot load", color=0xFD3333))


class CogUnloaderView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=20)

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
    def __init__(self):
        super().__init__(timeout=20)

    @discord.ui.select(
        placeholder="Reload",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=i) for i in getAllCogs()]
    )
    async def select_callback(self, select, interaction):
        try:
            interaction.client.reload_extension(select.values[0])
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Reloaded", color=0x00FF42))

        except:
            await interaction.response.edit_message(embed=discord.Embed(title=f"{select.values[0]} Not loaded", color=0xFD3333))


class CogManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    cogs = SlashCommandGroup("cog", "Managing cogs")

    @cogs.command(description="Load a single cog")
    async def load(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Loader", color=0x00FF42), view=CogLoaderView())

    @cogs.command(description="Unload a single cog")
    async def unload(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Unloader", color=0x00FF42), view=CogUnloaderView())

    @cogs.command(description="Reload a single cog")
    async def reload(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"Reloader", color=0x00FF42), view=CogReloaderView())

    @cogs.command(description="Reload all cogs")
    async def reloadall(self, ctx):
        for cog in getAllCogs():
            if cog == "src.cogs.dev.cogs.managing":
                continue

            try:
                self.bot.reload_extension(cog)

            except:
                continue

        await ctx.respond(embed=discord.Embed(title=f"All loaded cogs have been reloaded", color=0x00FF42))

    @cogs.command(description="Load all cogs")
    async def loadall(self, ctx):
        for cog in getAllCogs():
            try:
                self.bot.load_extension(cog)

            except:
                continue

        await ctx.respond(embed=discord.Embed(title=f"All cogs have been loaded", color=0x00FF42))

    @cogs.command(description="List all cogs")
    async def list(self, ctx):

        unloaded, loaded = "", ""
        all_cogs = getAllCogs()
        for i in all_cogs:
            if i not in self.bot.extensions:
                unloaded += i + "\n"
            else:
                loaded += i + "\n"

        embed = discord.Embed(title=f"Loaded cogs", color=0x00FF42)
        embed.add_field(name="Loaded cogs", value=loaded)
        embed.add_field(name="Unloaded cogs", value=unloaded)
        await ctx.respond(embed=embed)

    @cogs.command(description="List all cogs")
    async def testing(self, ctx):
        await ctx.respond(discord.AppInfo.guild)


def setup(bot):
    bot.add_cog(CogManagement(bot))
