import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
# indata: list of discord ids [id...]
# utdata: list of 2 teams, teams have list of discord ids [[id...],[id...]]


class removePlayer(discord.ui.View):
    @discord.ui.select(
        placeholder="Choose a player to remove",
        min_values=1,
        max_values=3,
        options=[
            discord.SelectOption(
                label="online",
                value='0'
            ),
            discord.SelectOption(
                label="offline",
                value='1'
            ),
            discord.SelectOption(
                label="idle",
                value='2'
            ),
            discord.SelectOption(
                label="dnd",
                value='3'
            )
        ]
    )
    async def select_callback(self, select, interaction):
        statuses = [discord.Status.online, discord.Status.offline,
                    discord.Status.idle, discord.Status.dnd, discord.Status.streaming]
        await interaction.client.change_presence(status=statuses[int(select.values[0])])
        await interaction.message.edit_message(embed=discord.Embed(title=f"Changed status to {statuses[int(select.values[0])]}", color=0x00FF42))


class LeagueRecommendTeams(commands.Cog):
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

        # select UI to delete poeple

        if len(list(ctx.author.voice.channel.members)) > 10:
            await ctx.respond(embed=discord.Embed(title="You need to be in a voice channel", color=0xFD3333))
            return

        ctx.author.voice.channel.members
        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Success', value='a')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(LeagueRecommendTeams(bot))
