from dis import disco
import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from pymongo import MongoClient


class manageCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    manageCommands = SlashCommandGroup(
        "managecommands", 'enable and disable commands for different roles')

    @manageCommands.command()
    async def enable(self, ctx, command: discord.Option(discord.SlashCommand), role: discord.Option(discord.Role) = None):
        if not role:
            role = ctx.guild.default_role
        roleId = role.id
        configColl = MongoClient('127.0.0.1', 27017).bjornbananv2.config
        query = {'type': 'manageCommands', 'guildId': ctx.guild_id}
        res = list(configColl.find_one(query))
        if not res:
            configColl.insert_one(query)
            res = query
        else:
            res = res[0]


def setup(bot):
    bot.add_cog(manageCommands(bot))
