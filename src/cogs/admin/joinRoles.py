import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from pymongo import MongoClient


async def defaultJoinRoles(member):
    guild = member.guild
    configColl = MongoClient('localhost', 27017).bjornbananv2.config
    query = {'type': 'joinRoles', 'guildId': guild.id}
    roles = list(configColl.find(query))

    if not roles:
        return

    for role in roles:
        roleObject = guild.get_role(role['roleId'])
        await member.add_roles(roleObject)


async def personalRoles(self, member):
    return


class joinRoles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    joinRolesGroup = SlashCommandGroup(
        "joinroles", 'Automaticly add roles to users who join')

    # enable/disable keepRolesOnLeave[]
    # add roles on join[]
    @joinRolesGroup.command()
    @commands.has_permissions(manage_roles=True)
    async def add(self, ctx, role: discord.Option(discord.Role, name='role')):
        if ctx.author.top_role.position < role.position:
            await ctx.respond(embed=discord.Embed(title="You dont have the permissions to add this role", color=0xFD3333))
            return

        configColl = MongoClient('127.0.0.1', 27017).bjornbananv2.config
        query = {'type': 'joinRoles',
                 'guildId': ctx.guild_id, 'roleId': role.id}
        roleAdded = configColl.find_one(query)
        if not roleAdded:
            configColl.insert_one(query)
            await ctx.respond(embed=discord.Embed(title=f"{role} added to joinroles", color=0x00FF42))
        else:
            await ctx.respond(embed=discord.Embed(title=f"{role} already added to joinroles", color=0xFD3333))

    @joinRolesGroup.command()
    @commands.has_permissions(manage_roles=True)
    async def remove(self, ctx, role: discord.Option(discord.Role, name='role')):
        if ctx.author.top_role.position < role.position:
            await ctx.respond(embed=discord.Embed(title="You dont have the permissions to add this role", color=0xFD3333))
            return
        configColl = MongoClient('localhost', 27017).bjornbananv2.config
        query = {'type': 'joinRoles',
                 'guildId': ctx.guild_id, 'roleId': role.id}
        roleAdded = configColl.find_one(query)
        if not roleAdded:
            await ctx.respond(embed=discord.Embed(title=f"{role} not in joinroles", color=0xFD3333))
        else:
            configColl.delete_one(query)
            await ctx.respond(embed=discord.Embed(title=f"{role} removed from joinroles", color=0x00FF42))

    @joinRolesGroup.command()
    async def show(self, ctx):
        configColl = MongoClient('localhost', 27017).bjornbananv2.config
        query = {'type': 'joinRoles', 'guildId': ctx.guild_id}
        roles = list(configColl.find(query))
        if not roles:
            await ctx.respond(embed=discord.Embed(title="There are no roles in joinroles", color=0x00FF42))
            return

        embed = discord.Embed(title="Joinroles", color=0x00FF42)
        for role in roles:
            roleObject = ctx.guild.get_role(role['roleId'])
            embed.add_field(name=f'{roleObject}', value="\u200b")
        await ctx.respond(embed=embed)

    persistent = SlashCommandGroup(
        "persistent", 'Automaticly add roles to users who leave and join')

    @persistent.command()  # FIXME waiting for rolelog
    async def enable(self, ctx):
        configColl = MongoClient('localhost', 27017).bjornbananv2.config
        query = {'type': 'keepRolesOnLeave', 'guildId': ctx.guild_id}
        keepRolesOnLeaveBool = list(configColl.find(query))
        if not keepRolesOnLeaveBool:
            configColl.insert_one(query)
            await ctx.respond(embed=discord.Embed(title="Enabled keepRolesOnLeave", color=0x00FF42))
            return
        await ctx.respond(embed=discord.Embed(title="Already enabled", color=0xFD3333))

    @persistent.command()  # FIXME waiting for rolelog
    async def disable(self, ctx):
        configColl = MongoClient('localhost', 27017).bjornbananv2.config
        query = {'type': 'keepRolesOnLeave', 'guildId': ctx.guild_id}
        keepRolesOnLeaveBool = list(configColl.find(query))
        if not keepRolesOnLeaveBool:
            await ctx.respond(embed=discord.Embed(title="Already disabled", color=0xFD3333))
            return
        configColl.delete_one(query)
        await ctx.respond(embed=discord.Embed(title="Disabled keepRolesOnLeave", color=0x00FF42))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        defaultJoinRoles(self, member)
        # personalRoles(self, member)  FIXME waiting for rolelog


def setup(bot):
    bot.add_cog(joinRoles(bot))
