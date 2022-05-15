import os
from dotenv import load_dotenv

from src.createBot import createBot
import src.cogs.dev.logging

load_dotenv()
bot = createBot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
