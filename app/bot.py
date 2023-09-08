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
        
    def on_message(self, *args, **kwargs):
        if self.is_ready():
            channel = self.get_channel(vars.DISCORD_CHANEL_ID)
            self.loop.create_task(channel.send("message"))

    async def on_ready(self):
        print("Bot is ready!")
        emitter.on(EVENT_WEBHOOK, self.on_message)

async def setup():
    client = Bot()

    async with client:
        await client.start(vars.DISCORD_TOKEN)