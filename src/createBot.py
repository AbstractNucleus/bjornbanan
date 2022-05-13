import discord
from discord.ext import commands

cogs = [
    'testing.fabian.exampleCog'
]


def createBot():
    bot = discord.Bot(debug_guilds=[802298523214938153], help_command=commands.MinimalHelpCommand()) 

    for cog in cogs:
        bot.load_extension(f'src.cogs.{cog}')

    @bot.command(description="Sends the bot's latency.") 
    async def ping(ctx): 
        await ctx.respond(f"Pong! Latency is {bot.latency}")
    return bot