import discord
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

file_handler = logging.FileHandler("log-file.txt")
file_handler.setLevel("DEBUG")

logger.addHandler(file_handler)

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    logger.debug(message)
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Fuck you!")


token = os.getenv("TOKEN")
client.run(token)
