import discord
from discord.ext import commands


class statusChoice(discord.ui.View):
    @discord.ui.select(
        placeholder="Choose a status",
        min_values=1,
        max_values=1,
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
        # await interaction.message.edit(embed=discord.Embed(title=f"Changed status to {statuses[int(select.values[0])]}", color=0x00FF42))
        # TODO this makes interactions fail. Needs to respond to not fail.
        await interaction.response.send_message(f"Changed status to {statuses[int(select.values[0])]}")


class presence(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def status(self, ctx):
        if not str(ctx.author.id) == "243022798543519745" and not str(ctx.author.id) == "212483159659380739":
            await ctx.respond(embed=discord.Embed(title="You dont have access to this command", color=0xFD3333))
            return
        await ctx.respond(embed=discord.Embed(title=f"Change presence", color=0x00FF42), view=statusChoice())


def setup(bot):
    bot.add_cog(presence(bot))
