from src.nbot import nbot
import os
from dotenv import load_dotenv

load_dotenv()
bot = nbot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
