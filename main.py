import asyncio

from app.http import app as flask_app
from app.bot import setup as setup_bot
from app.config import vars

def start_flask_app():
    flask_app.run(host='0.0.0.0', port=vars.HTTP_PORT)

async def main():
    loop = asyncio.get_event_loop()

    # Inicia el bot de discord en el loop actual
    loop.create_task(setup_bot())

    # Ejecuta Flask en el mismo loop
    await loop.run_in_executor(None, start_flask_app)

if __name__ == "__main__":
    asyncio.run(main())