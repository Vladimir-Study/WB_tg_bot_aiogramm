from config_data import config
from states import FeedbacksState
from handlers import other_router, user_router
from aiogram.fsm.storage.redis import Redis, RedisStorage
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher
from services.logger import logger

import asyncio


async def main() -> None:
    # redis: Redis = Redis(host="redis://localhost", decode_responses=True)
    #
    # storage: RedisStorage = RedisStorage(redis)
    logger.success("Bot was been started")

    bot: Bot = Bot(config.tg_bot.bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_router)
    dp.include_router(other_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    logger.success("Bot was been sroped")


asyncio.run(main())
