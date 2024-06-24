from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from dataclasses import dataclass
from envparse import Env
from aioredis import Redis, from_url


env: Env = Env()
env.read_envfile()


@dataclass
class DatabaseConfig:
    engine: AsyncEngine


@dataclass
class BotConfig:
    bot_token: str
    payment_token: str


@dataclass
class YandexConfig:
    token: str
    catalog_uid: str


@dataclass
class RedisConfig:
    redis: Redis


@dataclass
class Config:
    tg_bot: BotConfig
    db: DatabaseConfig
    yandex: YandexConfig
    redis: RedisConfig


config = Config(
    tg_bot=BotConfig(bot_token=env("BOT_TOKEN"), payment_token=env("PAYMENT_TOKEN")),
    db=DatabaseConfig(
        engine=create_async_engine(
            url=f"postgresql+asyncpg://{env('DB_USER')}:{env('DB_PASSWORD')}"
            f"@{env('DB_HOST')}:{env('DB_PORT')}/{env('DB_NAME')}",
            # echo=True,
        )
    ),
    yandex=YandexConfig(token=env("YANDEX_TOKEN"), catalog_uid=env("CATALOG_UID")),
    redis=RedisConfig(redis=from_url("redis://localhost", decode_responses=True)),
)
