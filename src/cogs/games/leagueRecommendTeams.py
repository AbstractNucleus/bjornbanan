import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
# indata: list of discord ids [id...]
# utdata: list of 2 teams, teams have list of discord ids [[id...],[id...]]


class leagueRecommendTeams(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    teamRecommendation = SlashCommandGroup(
        'teamrecommendation', 'Give custom games league recommendation')

    @teamRecommendation.command()
    async def teamRecommendation(self, ctx):
        # get users in channel plus @user
        if not ctx.author.voice:
            await ctx.respond(embed=discord.Embed(title="You need to be in a voice channel", color=0xFD3333))
            return

        users = []
        for user in ctx.author.voice.channel.members:
            if user.bot:
                continue
            users.append(user)

        if len(list(ctx.author.voice.channel.members)) > 10:
            await ctx.respond(embed=discord.Embed(title="You need to be in a voice channel", color=0xFD3333))
            return

        ctx.author.voice.channel.members
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Success', value='a')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(leagueRecommendTeams(bot))
