import random
import settings
# Normal Packages import for discord
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():

    # A factory method that creates a Intents with everything enabled except presences, members, and message_content.
    intents = discord.Intents.default()
    intents.message_content = True
    # bot is variable which is the bot for this example
    bot = commands.Bot(command_prefix="!", intents=intents)
   
    #Called when the client is done preparing the data received from Discord.
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")
                 




    bot.run(settings.DISCORD_API_SECRET, root_logger=True) 

if __name__ == "__main__": 
    run()

