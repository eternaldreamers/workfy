import asyncio

from app.http import setup as setup_http

async def main():
    await setup_http()

if __name__ == "__main__":
  asyncio.run(main())