from src.createBot import createBot
import os
from dotenv import load_dotenv

load_dotenv()
if not os.getenv('PREFIX'):
    prefix = '.'
else:
    prefix = os.getenv('PREFIX')

bot = createBot(prefix)

if __name__ == '__main__':
    bot.run(os.getenv('TOKEN'))
