from src.nbot import nbot
import os
from dotenv import load_dotenv

load_dotenv()
if not os.getenv('PREFIX'):
    prefix = '.'
else:
    prefix = os.getenv('PREFIX')


if __name__ == '__main__':
    nbot().run(os.getenv('TOKEN'))
