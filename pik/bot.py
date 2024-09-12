import asyncio
import logging
from aiogram import Bot, Dispatcher

from app.obr import router


bot = Bot(token='pip')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")