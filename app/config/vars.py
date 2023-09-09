import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_CHANEL_ID = int(os.environ.get("DISCORD_CHANEL_ID"))

ASANA_TOKEN=os.environ.get("ASANA_TOKEN")

HTTP_PORT = int(os.environ.get("HTTP_PORT"))