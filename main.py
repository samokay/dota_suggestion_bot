import logging
import os

import discord
from dotenv import load_dotenv

import dotabuff_scrapper

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

file_handler = logging.FileHandler("log-file.txt", mode="w")
file_handler.setLevel("DEBUG")

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
        if message.content.startswith("$heroes "):
            bans_splitter_char = "|"
            heroes = message.content[7:]
            picks, bans = heroes.split(bans_splitter_char)
            picks, bans = picks.strip().split(","), bans.strip().split(",")
            await message.channel.send(dotabuff_scrapper.get_suggestions(picks, bans))
        if message.content.startswith("$spells "):
            hero_name = message.content[7:].strip()
            spells_result = dotabuff_scrapper.get_heroes_spells(hero_name)
            for spell_name, stats in spells_result:
                await message.channel.send(f"{spell_name}\n{stats}\n")

    def run(self):
        super().run(self.token)


bot = DotaClient(os.getenv("TOKEN"))
bot.run()
