import discord
from discord.ext import commands
from time import time
from datetime import timedelta


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time()

    @discord.command(description="Returns information about the server")
    async def server(self, ctx):
        embed = discord.Embed(title=ctx.guild.name,
                              description=ctx.guild.description, color=0x00FF42)
        invites = await ctx.guild.invites()

        embed.add_field(name="Owner", value=ctx.guild.owner)
        embed.add_field(name="ID", value=ctx.guild.id)
        embed.add_field(name="Invites", value="".join(f"{i.url}\n" for i in invites))
        embed.add_field(name="Member count", value=ctx.guild.member_count)
        embed.add_field(name="Creation Date", value=ctx.guild.created_at)
        embed.add_field(name="Text channels", value=len(ctx.guild.text_channels))
        embed.add_field(name="Voice channels", value=len(ctx.guild.voice_channels))
        embed.add_field(name="Number of categories", value=len(ctx.guild.categories))
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)
        embed.set_image(url=ctx.guild.icon)

        await ctx.respond(embed=embed)

    @discord.command(description="Returns information about the user")
    async def user(self, ctx, user: discord.Option(discord.Member)):
        embed = discord.Embed(title=user.name+user.discriminator, color=user.color)

        embed.add_field(name="ID", value=user.id)
        embed.add_field(name="Nickname", value=user.nick)
        embed.add_field(name="Creation Date", value=str(user.created_at)[:10])
        embed.add_field(name="Join Date", value=str(user.joined_at)[:10])
        embed.add_field(name="Roles", value="".join(
            f"{i.name}    " for i in user.roles), inline=False)
        embed.set_author(name=user.name, icon_url=user.avatar)
        embed.set_image(url=user.avatar)

        await ctx.respond(embed=embed)

    @discord.command(description="Returns information about the bot")
    async def bot(self, ctx):
        bot = await self.bot.application_info()
        embed = discord.Embed(title=bot.name, description=self.bot.description,
                              color=self.bot.user.color)

        embed.add_field(name='ID', value=bot.id)
        embed.add_field(name='Guilds', value=len(self.bot.guilds))
        embed.add_field(name='Users', value=len(self.bot.users))
        embed.add_field(name='Commands', value=len(self.bot.commands))
        embed.add_field(name='Emojis', value=len(self.bot.emojis))
        embed.add_field(name='Latency', value=round(self.bot.latency*1000, 1))
        embed.add_field(name='Source code',
                        value="https://github.com/AbstractNucleus/bjornbanan", inline=False)
        embed.set_author(name=bot.name, icon_url=bot.icon)
        embed.set_image(
            url=bot.icon)

        await ctx.respond(embed=embed)

    @discord.command(description="Returns latency of the bot")
    async def ping(self, ctx):
        await ctx.respond(embed=discord.Embed(title=f"{round(self.bot.latency*1000, 1)} ms", color=0x00FF42))

    @discord.command(description="Returns the uptime of the bot")
    async def uptime(self, ctx):
        differenceInTime = time()-self.start_time
        text = str(timedelta(seconds=differenceInTime))
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Uptime', value=text)
        await ctx.respond(embed=embed)

    @discord.command(description="Returns all server invites")
    async def invites(self, ctx):
        invites = await ctx.guild.invites()
        await ctx.respond(embed=discord.Embed(title="".join(f"{i.url}\n" for i in invites), color=0x00FF42))


def setup(bot):
    bot.add_cog(Info(bot))
