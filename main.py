import asyncio
import threading

from app.http import setup as setup_http
from app.bot import setup as setup_bot

def thread_func():
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(setup_bot())
  loop.close()

async def main():
  thread = threading.Thread(target=thread_func)
  thread.start()

  await setup_http()

if __name__ == "__main__":
  asyncio.run(main())