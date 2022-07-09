import discord

bot = discord.Bot()


class MyView(discord.ui.View):
    @discord.ui.select(  # the decorator that lets you specify the properties of the select menu
        # the placeholder text that will be displayed if nothing is selected
        placeholder="Choose a Flavor!",
        min_values=1,  # the minimum number of values that must be selected by the users
        max_values=1,  # the maxmimum number of values that can be selected by the users
        options=[  # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="Vanilla",
                description="Pick this if you like vanilla!"
            ),
            discord.SelectOption(
                label="Chocolate",
                description="Pick this if you like chocolate!"
            ),
            discord.SelectOption(
                label="Strawberry",
                description="Pick this if you like strawberry!"
            )
        ]
    )
    # the function called when the user is done selecting options
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!")


@bot.command()
async def flavor(ctx):
    await ctx.send("Choose a flavor!", view=MyView())

bot.run("TOKEN")
