import discord


def nbot():
    bot = discord.Bot(debug_guilds=[802298523214938153])

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready and online!")

    return bot
