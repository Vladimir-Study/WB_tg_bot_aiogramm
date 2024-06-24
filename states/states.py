# import asyncio
# import aioredis
from aiogram.fsm.state import State, StatesGroup


class FeedbacksState(StatesGroup):
    fb_not_answer: State = State()
    fb_answered: State = State()


# async def redis():
#     async with aioredis.from_url("redis://localhost", decode_responses=True) as redis:
#         await redis.hset(
#             "hash", mapping={"key1": "value1", "key2": "value2", "key3": 123}
#         )
#         result = await redis.hgetall("hash")
#         print(result)
#         assert result == {"key1": "value1", "key2": "value2", "key3": "123"}
#
#
# if __name__ == "__main__":
#     asyncio.run(redis())
