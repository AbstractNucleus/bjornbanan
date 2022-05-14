# Embed templates

## Basic

### Success

        await ctx.respond(embed=discord.Embed(title="Success", color=0x00FF42))

### Failure

        await ctx.respond(embed=discord.Embed(title="Failure", color=0xFD3333))

## More complex

### Success

        embed = discord.Embed(color=0x00FF42)
        embed.add_field(name='Success', value='a')
        await ctx.respond(embed=embed)

### Failure

        embed = discord.Embed(color=0xFD3333)
        embed.add_field(name='Failed', value='a')
        await ctx.respond(embed=embed)
