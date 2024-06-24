from aiohttp.web_response import Response
from envparse import Env
from WB_feedbacks import WBParser
from yandex_AI import YandexAI
from pprint import pprint

import asyncio
import aioredis


env = Env()
env.read_envfile()


class FeedbacksRedis:
    pass


class GenerateFeedbacks:
    def __init__(self, response: dict):
        self.response = response

    async def create_feedback_dict(
        self, message_id: int, is_publish: bool, uid: int
    ) -> dict:
        company = self.response.get("productDetails").get("brandName")
        created_date = self.response.get("createdDate")
        product_name = self.response.get("productDetails").get("productName")
        product_valuation = self.response.get("productValuation")
        feedback_id = self.response.get("id")
        user_name = self.response.get("userName")
        text_feedback = self.response.get("text")
        ai_answer = await self.get_ai_answer(
            text_feedback, company, user_name, product_name
        )
        product_valuation = await self.convert_product_valuation(product_valuation)
        return {
            "message_id": message_id,
            "feedback_id": feedback_id,
            "company": company,
            "product_name": product_name,
            "product_valuation": product_valuation,
            "created_date": created_date,
            "text_feedback": text_feedback,
            "ai_answer": ai_answer,
            "is_publish": is_publish,
            "uid": uid,
        }

    async def get_ai_answer(
        self, text_feedback: str, company: str, user_name: str, product_name: str
    ) -> str:
        ya_ai = YandexAI(env("YANDEX_TOKEN"))
        ai_feedback = await ya_ai.create_feetbacks(
            text_feedback, company, user_name, product_name
        )
        ai_answer = (
            ai_feedback.get("result").get("alternatives")[0].get("message").get("text")
        )
        return ai_answer

    async def convert_product_valuation(self, product_valuation: str) -> str:
        text_product_valuation = ""
        for index in range(1, 6, 1):
            if index <= int(product_valuation):
                text_product_valuation += "⭐️"
            else:
                text_product_valuation += "♦️"
        return text_product_valuation


async def main() -> None:
    feedback = WBParser(env("WB_TOKEN"))
    response = await feedback.get_feedback()
    pprint(response)
    test = GenerateFeedbacks(response.get("data").get("feedbacks")[0])
    result = await test.create_feedback_dict(123, False, 321)
    pprint(result)


if __name__ == "__main__":
    asyncio.run(main())
