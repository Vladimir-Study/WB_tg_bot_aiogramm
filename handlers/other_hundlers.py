from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import FeedbacksState


router: Router = Router()


@router.message()
async def test_redis(message: Message, state: FSMContext) -> None:
    data = {"test1": "test1", "test2": "test2"}
    await state.set_data(data=data)
    await state.set_state(FeedbacksState.fb_not_answer)
    await state.set_data(data={"ret": "ter"})
    print(await state.get_data())
    await message.answer(data["test1"])
