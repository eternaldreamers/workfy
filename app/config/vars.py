import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

HTTP_PORT = int(os.environ.get("HTTP_PORT"))