import createBot
import os
from dotenv import load_dotenv

load_dotenv()
bot = createBot()

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
