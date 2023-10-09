import discord
from discord.ext import commands


#___________________________________________________________________________________


@commands.group()
# This is a function or group commands called (math) that will group all math oprations
async def math(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"No, {ctx.subcommand_passed} does not belong to math")


# A command function for adding two nembers 
@math.command()
async def add(ctx, one : int , two : int ):
        await ctx.send(one+two)

# A command function for adding two nembers 
@math.command()
async def sub(ctx, one : int , two : int ):
        await ctx.send(one-two)

# A command function for adding two nembers 
@math.command()
async def div(ctx, one : int , two : int ):
        await ctx.send(one/two)

# A command function for adding two nembers 
@math.command()
async def mult(ctx, one : int , two : int ):
        await ctx.send(one*two)


#___________________________________________________________________________________


async def setup(bot):
        bot.add_command(math)
        
