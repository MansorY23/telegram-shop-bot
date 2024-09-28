import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher

from shop_bot.utils import logger, BotConfig, DBConfig, RedisConfig
from shop_bot.handlers import commands
from shop_bot.keyboards import set_main_menu
from shop_bot.middlewares import DBSessionMiddleware
from shop_bot.db import create_pool


async def main():
    logger.info('Starting bot')
    bot_config: BotConfig = BotConfig()
    db_config: DBConfig = DBConfig()
    redis_config = RedisConfig()
    redis: Redis = Redis(host=redis_config.host,
                         port=redis_config.port,
                         db=redis_config.db)
    bot: Bot = Bot(
        token=bot_config.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    if redis_config.use_redis is True:
        storage = RedisStorage(redis=redis)
    else:
        storage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_routers(commands.router)

    dp.update.middleware(DBSessionMiddleware(session_pool=create_pool(db_config)))
    dp.workflow_data.update({'admin_ids': bot_config.admins_ids_to_list()})
    await set_main_menu(bot=bot)
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())