from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from states import SetTimeDeltaState
from lexicon import LEXICON_RU


router = Router()


@router.callback_query(F.data == "time_self", StateFilter(default_state))
async def proccess_set_self_time_step_one(
    callback: CallbackQuery, state: FSMContext
) -> None:
    await callback.message.answer(text=LEXICON_RU["self_edit_time"])
    await state.set_state(SetTimeDeltaState.time_not_set)
    await callback.answer()


@router.message(StateFilter(SetTimeDeltaState.time_not_set))
async def proccess_set_self_time_step_two(message: Message, state: FSMContext) -> None:
    text = message.text.split(" ")
    flag = (
        True
        if len(text) == 3 and text[0].isdigit() and text[2].isdigit() and text[1] == "-"
        else False
    )
    if flag:
        if int(text[0]) <= 23 and int(text[2]) <= 23:
            await message.answer(LEXICON_RU["time_success_edit"])
            await state.clear()
        else:
            await message.answer(LEXICON_RU["time_delta_error"])
    else:
        await message.answer(LEXICON_RU["time_format_error"])
