import discord
from discord.ext import commands
from app.config import vars
from app.config.constants import EVENT_WEBHOOK
from app.config.events import emitter

intents = discord.Intents.all()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="?", intents=intents)
        
    def on_message_event(self, message):
        if self.is_ready():
            channel = self.get_channel(vars.DISCORD_CHANEL_ID)

            embed = discord.Embed(title=message.get("assignee"), color=0xee6a6a)
            embed.set_author(name="Asana", icon_url=message.get("logo"))
            embed.add_field(name="Action", value=message.get("action"))
            embed.add_field(name="Points", value=message.get("points"))
            embed.add_field(name="Name", value=message.get("name"))
            embed.add_field(name="Notes", value=message.get("notes"))
            embed.add_field(name="Due At", value=message.get("due_at"))
            embed.add_field(name="Due On", value=message.get("due_on"))

            self.loop.create_task(channel.send(embed=embed))

    async def on_ready(self):
        print("Bot is ready!")
        emitter.on(EVENT_WEBHOOK, self.on_message_event)

async def setup():
    client = Bot()

    async with client:
        await client.start(vars.DISCORD_TOKEN)