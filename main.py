from src.nbot import nbot
import os
from dotenv import load_dotenv

load_dotenv()
if os.getenv('PREFIX'):
    prefix = os.getenv('PREFIX')
else:
    prefix = '.'


if __name__ == '__main__':
    nbot(prefix).run(os.getenv('TOKEN'))
