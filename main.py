import discord
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

file_handler = logging.FileHandler('log-file.txt', mode='w')
file_handler.setLevel('DEBUG')

logger.addHandler(file_handler)

client = discord.Client()


class DotaClient(discord.Client):

    def __init__(self, token):
        super().__init__()
        self.token = token

    async def on_ready(self):
        logger.info(f"We have logged in as {self.user.name}")
        logger.debug(self)

    async def on_message(self, message):
        logger.debug(message)
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Fuck you!')

    def run(self):
        super().run(self.token)


bot = DotaClient(os.getenv("TOKEN"))
bot.run()
