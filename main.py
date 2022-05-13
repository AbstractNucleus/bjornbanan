<<<<<<< HEAD
from src.nbot import nbot
=======
from src.createBot import createBot
>>>>>>> bc9d729551273a128e5721d0f982f7e8cdf46ba5
import os
from dotenv import load_dotenv

load_dotenv()
bot = nbot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
