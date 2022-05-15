import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from ...lib.perms import isOwner, PermissionDeniedEmbed

load_dotenv()


class statusChoice(discord.ui.View):
    statuses = ["online", "offline", "do not disturb", "idle", "streaming"]

    @discord.ui.select(
        placeholder="Choose a status",
        min_values=1,
        max_values=1,
        options=[discord.SelectOption(label=j, value=str(i)) for i, j in enumerate(statuses)]
    )
    async def select_callback(self, select, interaction):
        statuses = [discord.Status.online, discord.Status.offline,
                    discord.Status.dnd, discord.Status.idle, discord.Status.streaming]
        await interaction.client.change_presence(status=statuses[int(select.values[0])])
        await interaction.response.edit_message(embed=discord.Embed(title=f"Changed status to {statuses[int(select.values[0])]}", color=0x00FF42))


class presence(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def presence(self, ctx):
        if not isOwner(ctx.author.id):
            await PermissionDeniedEmbed(ctx)
            return

        await ctx.respond(embed=discord.Embed(title=f"Change presence", color=0x00FF42), view=statusChoice())


def setup(bot):
    bot.add_cog(presence(bot))
