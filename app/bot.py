import os
import discord
import asyncio
from discord.ext import commands
from app.config import vars
from app.config.constants import EVENT_WEBHOOK
from app.config.events import emitter

intents = discord.Intents.all()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="?", intents=intents)

    async def on_ready(self):
        print("ready!!!")

        def on_message(message):
            print("df")
            # if self.is_ready():
            #     channel = self.get_channel(vars.DISCORD_CHANEL_ID)
            #     await channel.send(message)

            emitter.on(EVENT_WEBHOOK, on_message)

async def setup():
    client = Bot()

    async with client:
        await client.start(vars.DISCORD_TOKEN)